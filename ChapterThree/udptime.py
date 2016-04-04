import socket
import sys
import struct
import time


port = 51423

host = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes('', encoding='utf-8'), (host, port))

print("Looking for replies; press Ctrl-C to stop.")

buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print("Wrong-sized reply %d: %s" % (len(buf), buf))
    sys.exit(1)
secs = struct.unpack("!I", buf)[0]
secs -= 2208988800
print(time.ctime(int(secs)))
