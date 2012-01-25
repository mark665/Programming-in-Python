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

input = [s, sys.stdin]

print "Enter text to send : "
while True :
    inputready,outputready,exceptready = select.select(input,[],[],timeout)
    for selectInput in inputready:
        if selectInput == sys.stdin:
            text = str(raw_input('> '))
            if text : 
                s.send(text) 
            else :
                s.close() 
                break        
        if selectInput == s:
            text = s.recv(size)
            print text


