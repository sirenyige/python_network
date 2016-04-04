#-*- coding: UTF-8 -*-

import socket
import sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except socket.gaierror as e:
    print("Error connecting to server: %s" % e)
    sys.exit(1)

fd = s.makefile('rwb', 0)
fd.write(filename.encode('utf-8')+"\r\n".encode('utf-8'))
for line in fd.readlines():
    sys.stdout.write(line.decode('utf-8'))

# bdata = bytes(filename+"\r\n", encoding="utf-8")
# s.sendall(bdata)

# while 1:
#    buf = s.recv(2048)
#    if not len(buf):
#        break
#    sys.stdout.write(str(buf, encoding="utf-8"))
