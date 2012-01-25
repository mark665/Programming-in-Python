"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50001 
size = 1024 
text = ''

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
s.connect((host,port))
print 'Connection accepted by (%s,%s)' % (host, port)
print "Enter test to send : "
while True :
    text = str(raw_input('> '))
    if text : 
        s.send(text) 
        data = s.recv(size)
        print data
    else :
        s.close() 
        print 'from (%s,%s) %s' % (host, port, data)
        break
