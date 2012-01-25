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
size = 1024 
text = ''
timeout = 10 # seconds

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

#open socket for sending to the server
s = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
s.connect((host,port))

#open socket for recieving from the server
backlog = 5
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
r.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

r.bind((host,port))
r.listen(backlog)

input = [r,sys.stdin]

while True :
    print "Enter test to send : "
    inputready,outputready,exceptready = select.select(input,[],[],timeout)
    for input in inputready:
        if input == sys.stdin:
            text = str(raw_input())
            s.send(text)
        if input == r:
            print r.recv(size)
            
s.close()
r.close

