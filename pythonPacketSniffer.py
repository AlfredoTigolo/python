#!/usr/local/bin/python3

#only works on a live linux box and does not work under Windows Subsystem Linux
#Source https://www.binarytides.com/python-packet-sniffer-code-linux/

#Packet sniffer in python
#sniffs only incoming tcp packet

import socket, sys
from struct import *

#define ETH_P_ALL=0x0003

#create an INET, raw socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP )
    #s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except socket.error:
    print ("Socket could not be created. Error Code :" + str(msg[0]) + " Message " + str(msg[1]) )
    sys.exit()

# receive a packet
while True:
    #print ( s.recvfrom(65565) )
    packet = s.recvfrom(65565) 

    #packet from tuple
    packet = packet[0]

    #take first 20 characters for the ip header
    ip_header = packet[0:20]

    #now unpack them
    iph = unpack ('!BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);

    print ("Version : " + str(version) + " IP Header Length : " + str(ihl)) 
    print ("TTL :" + str(ttl) + " Protocol : " + str(protocol) )
    print ("Source Address :" + str(s_addr) + " Destination Address " + str(d_addr))

    tcp_header = packet[iph_length:iph_length+20]

    #now unpack them 
    tcph = unpack('!HHLLBBHHH', tcp_header)

    source_port = tcph[0]
    dest_port = tcph[1]
    sequence = tcph[2]
    acknowledgement = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4

    print ("Source Port : " + str(source_port) + " Dest Port : " + str(dest_port) + " Sequence Number : " + str(sequence) )
    print ("Acknowledgement :" + str(acknowledgement) + " TCP header length : " + str(tcph_length))

    h_size = iph_length + tcph_length * 4
    data_size = len(packet) - h_size
    
    #get data from the packet
    data = packet[h_size:]

    print ("Data : ")
    #print (data)
    print (" ") 
