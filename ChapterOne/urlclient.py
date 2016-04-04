import urllib.request
import sys

host = sys.argv[1]
file = sys.argv[2]

f = urllib.request.urlopen('http://%s%s' % (host, file))

for line in f.readlines():
    sys.stdout.write(line.decode('utf-8'))
