import redislite
from django.views.generic import TemplateView


class Result(object):

    command = None
    stdout = None
    stderr = None
    _returncode = None

    def __str__(self):
        return self.env

    def __repr__(self):
        return self.env

    @property
    def returncode(self):
        if self._returncode is None:
            return None
        return int(self._returncode)

class StatusDetail(TemplateView):
    template_name = "status.html"

    def get_context_data(self, **kwargs):
        redis_db = redislite.Redis('/tmp/tixtox.db')
        context={
            'envs': [],
        }
        env_list = []
        for tox_operations in redis_db.keys('tixtox:*:stdout'):
            result = Result()
            result.command = tox_operations.replace('tixtox:', '').replace(':stdout', '')
            result.env = tox_operations.replace('tox -e', '').strip()
            result.stdout = []
            for line in redis_db.lrange(tox_operations, 0, -1):
                if line.strip():
                    result.stdout.append(line.strip())
            result._returncode = redis_db.get(
                tox_operations.replace(':stdout', ':returncode')
            )
            print(result.command, result.returncode)
            env_list.append(result)
        env_list.sort(key=lambda x: x.env)
        context['envs'] = env_list
        print(context['envs'])
        return context
