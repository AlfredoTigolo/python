#!/usr/bin/python3

#only works on a live linux box and does not work under Windows Subsystem Linux
#Source https://www.binarytides.com/python-packet-sniffer-code-linux/

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP )

# receive a packet
while True:
    print ( s.recvfrom(65565) )
