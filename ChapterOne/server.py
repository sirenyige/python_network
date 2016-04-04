import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)


print("Server is running on port %d; press Ctrl-C to terminate." % port)

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rwb', 0)
    clientfile.write("Welcome, ".encode('utf-8') + str(clientaddr).encode('utf-8') + "\n".encode('utf-8'))
    clientfile.write("Please enter a string: \n".encode('utf-8'))
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n".encode('utf-8') % len(line))
    clientfile.close()
    clientsock.close()
