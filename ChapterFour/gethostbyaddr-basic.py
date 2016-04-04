import sys
import socket

try:
    result = socket.gethostbyaddr(sys.argv[1])
    print("Primary hostname:")
    print(" " + result[0])
    print("\nAddressess:")
    for item in result[2]:
        print(" " + item)
except socket.herror as e:
    print("Couldn't look up name:", e)
