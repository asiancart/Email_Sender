import sys
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets, QtWidgets

app = QtWidgets.QApplication(sys.argv)

web = QtWebEngineWidgets.QWebEngineView()
web.load(QtCore.QUrl("https://www.google.com"))

# Create toolbar and buttons
toolbar = QtWidgets.QToolBar()
back_button = QtWidgets.QAction("Back", web)
forward_button = QtWidgets.QAction("Forward", web)
refresh_button = QtWidgets.QAction("Refresh", web)

# Connect buttons to functionality
back_button.triggered.connect(web.back)
forward_button.triggered.connect(web.forward)
refresh_button.triggered.connect(web.reload)

# Add buttons to toolbar
toolbar.addAction(back_button)
toolbar.addAction(forward_button)
toolbar.addAction(refresh_button)

# Create layout
layout = QtWidgets.QVBoxLayout()
layout.addWidget(toolbar)
layout.addWidget(web)

# Create main window
main_window = QtWidgets.QMainWindow()
main_window.setCentralWidget(QtWidgets.QWidget(main_window))
main_window.centralWidget().setLayout(layout)

# Show main window
main_window.show()

sys.exit(app.exec_())