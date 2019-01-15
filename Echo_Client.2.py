#!/usr/bin/env python3

import socket
import time

HOST = '192.168.0.100'  # The server's hostname or IP address
PORT = 9600        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'run Lights50 \r\n')
host = socket.gethostname()
data = s.recv(1024)

time.sleep(1)
print('Received', repr(data))
new_name = ''

def move(): #Funksjon
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(b'run Lights50 \r\n')
    host = socket.gethostname()
    data = s.recv(1024)
    time.sleep(1)
    print('Received', repr(data))
    print("Test.")

func_dict = {'move':move}
if __name__ == "__main__":
    input("Trykk ENTER for og starte.")
    lightsOff = "lyset Av" #getNewEnvironment(environments)
    lightsOn = "lyset På" #getTime(timeTicks, timeOfDay)
    print("Ønsker du og skru {0}. Eller skru {1}.".format(lightsOff, lightsOn))
    command = input(host +" > ")
    func_dict[command]()
