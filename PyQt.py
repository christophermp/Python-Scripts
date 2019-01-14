import sys
import socket
from PyQt5 import QtCore, QtGui, uic
 
qtCreatorFile = "Jnior_Python3.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.sendCommand.clicked.connect(self.commandSend)
		
    def commandSend(self):
        HOST = '192.168.0.100'  # The server's hostname or IP address
        PORT = 9600        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'run Lights50\r\n')
        data = s.recv(1024)

print('Received', repr(data))

 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
