# Offensive Cyber Tools For Offensive Security/Penetration Testing Assignments 
# Connect on LinkedIn  https://www.linkedin.com/in/lismore or Twitter @patricklismore
#=========================================================================================================================================

#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

# Get user input
remoteServer    = raw_input("Enter target host to port scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print "-" * 50
print "Port Scanning your target", remoteServerIP
print "-" * 50

# Log Port Scan Start Time
startTime = datetime.now()

# Scan the first 1025 ports
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print "|- Port: ", port
        result = sock.connect_ex((remoteServerIP, port))
        #print "|- Result: ", result
        if result == 0:
            print "Target - Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Ctrl+C -- Stopping Port Scan"
    sys.exit()

except socket.gaierror:
    print 'Target ip could not be resolved. Stopping'
    sys.exit()

except socket.error:
    print "unable to connect to target machine"
    sys.exit()

# Log the port scan end time
endTime = datetime.now()

# Lpg port scan running time
runningTime =  endTime - startTime

# Printing the information to screen
print 'Port Scan Completed in: ', runningTime
