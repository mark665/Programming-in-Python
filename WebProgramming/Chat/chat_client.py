"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys
import select

host = 'localhost' 
port = 50003
backlog = 5
size = 1024 
text = ''
timeout = 10 # seconds

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

serv = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv.bind((host,port))

print 'echo_server listening on port %s, to exit type return ' % port
serv.listen(backlog)

serv.connect((host,port))
serv.accept()
input = [serv,sys.stdin]

while True :
    print "Enter test to send : "
    inputready,outputready,exceptready = select.select(input,[],[],timeout)
    
    for s in inputready:
        if s == sys.stdin:
            text = str(raw_input())
            serv.send(text) 
    
    data = s.recv(size) 

    print '%s' % (data)
s.close() 

