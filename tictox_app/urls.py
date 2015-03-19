from django.conf.urls import patterns, include, url
from .views import StatusDetail


urlpatterns = patterns('',
    url(r'^$', StatusDetail.as_view()),
)