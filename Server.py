import socket
import sys

"""
function for creating a socket
socket is used to connect 2 computers
"""


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999  # use this port because it is not common it is unique.
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error " + str(msg))


# Binding the socket and waiting for responce
def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding the por' + str(port))
        s.bind((host, port))
        # here 5 means it will tolerate the 5 errors after that it will give error
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error" + str(msg) + '\n' + 'Retrying..')
        bind_socket()


# Establish the connection with a client (socket must be listening for working)
def socket_accept():
    # It returns the 2 value connection and address
    connection, address = s.accept()
    print('Connection ahs been established! |' + 'IP' + address[0] + ' | port ' + str(address[1]))

    # sending commands to the client
    send_commands(connection)

    connection.close()

# send commands to the friends or client
def send_commands(connection):
    while True:
        cmd = input()
        if cmd == 'quit':
            connection.close()
            s.close()
            # closing the command promp
            sys.exit() 
        # when we send data from one computer to other it will be send in bytes not in string
        # converting the code in bytes 
        if len(str.encode(cmd)) > 0:
            # Here send is a function
            connection.send(str.encode(cmd))
            # Here 1024 is a size of chucks and utf-8 refers to the coding type
            client_responce = str(connection.recv(1024),'utf-8')
            print(client_responce, end = "")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()