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
# s.connect((host, port))
bdata = bytes(filename+"\r\n", encoding="utf-8")
s.sendall(bdata)

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(str(buf, encoding="utf-8"))
