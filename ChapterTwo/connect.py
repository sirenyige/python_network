import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Done")

print("Connecting to remote host...")
s.connect(("www.baidu.com", 80))
print("Done")
