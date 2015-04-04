import os
import sys
  
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

from PyQt5.uic import loadUi

app = QApplication(sys.argv)
ui_file = os.path.join(
    os.path.dirname(__file__),
    'tictox.ui'
)
window = loadUi(ui_file)
window.show()
sys.exit(app.exec_())
