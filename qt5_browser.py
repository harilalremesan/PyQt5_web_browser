import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
wv = QWebEngineView()
wv.load(QUrl("https://www.youtube.com"))
wv.show()
app.exec_()