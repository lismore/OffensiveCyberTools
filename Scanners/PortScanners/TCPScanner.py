#!/usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

destinationip = "192.168.1.1"
sourceport = RandShort()
destinationport=22
 
tcpConnectScabResp = sr1(IP(dst=destinationip)/TCP(sport=sourceport,dport=destinationport,flags="S"),timeout=10)
if(str(type(tcpConnectScabResp))=="<type 'NoneType'>"):
print "Closed"
elif(tcpConnectScabResp.haslayer(TCP)):
if(tcpConnectScabResp.getlayer(TCP).flags == 0x12):
send_rst = sr(IP(dst=destinationip)/TCP(sport=sourceport,dport=destinationport,flags="AR"),timeout=10)
print "Open"
elif (tcpConnectScabResp.getlayer(TCP).flags == 0x14):
print "Closed"
