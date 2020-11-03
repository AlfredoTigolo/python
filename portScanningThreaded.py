#!/usr/bin/python3
#source https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

import socket
import time
import threading

from queue import Queue 
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input ('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

#net = input("Enter the IP address: ")
net = target
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      con = s.connect((t_IP, port))
      with print_lock:
          print (port, 'is open on ip ', t_IP)
      con.close()
    except:
        pass 

def scan(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try: 
      socket.setdefaulttimeout(0.25)
      result = s.connect_ex((addr,135))
      if result == 0:
            return 1
      else :
            return 0
        #with print_lock:
          #s.close()
          #print (addr, 'is alive')        
    except:
        pass
   

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        #scan(target)
        q.task_done()

def threader2():
    while True:
        #for ip in range ( st1, en1 ):
        addr = net2 + str(1)
        if ( scan(addr) ):
            print (addr, " is alive")

q = Queue()
startTime = time.time()

for x in range (100):
    #t2 = threading.Thread( target = threader2 )
    #t2.daemon = True
    #t2.start()
    t = threading.Thread( target = threader )
    t.daemon = True
    t.start()    

for worker in range (1, 500):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)

for ip in range ( st1, en1 ):
    addr = net2 + str(ip)
    if ( scan ( addr )):
        print ( addr, " is alive")
