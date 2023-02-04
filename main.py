import sys
from PyQt5.QtWidgets import (
    QApplication,
)

from window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
exit_code = app.exec()
sys.exit(exit_code)
