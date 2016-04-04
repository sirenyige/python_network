import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Done")

print("Looking up port number...")
port = socket.getservbyname('http', 'tcp')
print("Done")

print("Connecting to remote host...", port)
s.connect(("www.baidu.com", port))
print("Done")

print("Connected from", s.getsockname())
print("Connected to", s.getpeername())
