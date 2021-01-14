#!/usr/local/bin/python3
#/usr/bin/python3.6

#source https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

from sys import argv
from socket import *
import time

startTime = time.time()

#using python3 portScanning -v to show verbose flags
verbose = False
try:
    flag = argv[1] 
    if ( flag == '-v') :
        verbose = True
    elif ( flag == '') :
        verbose = False
except:
#   print (str(verbose) + ' is verbose?')
    pass

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)    
    print ('Starting scan on host: ', t_IP)

    #i stands for ports
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        if ( verbose == True) :
            print ( 'i ' + str(i))
            print ( 'socket ' + str(s) )

        conn = s.connect_ex((t_IP, i))
        if ( verbose == True ) :
            print ( 'socket.connect ' + str(conn) )

        if (conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()
print ('Time taken:', time.time() - startTime)
