import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ('localhost', 10000)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    while True:

        try:
            print >> sys.stderr, 'connection from', client_address

            # receive the data in small chunks and retransmit it
            while True:
                selection = connection.recv(1)
                print >> sys.stderr, 'received "%s"' % selection
                if selection == '1':
                    message = 'showing contents of current directory:'
                    connection.sendall(message)
                elif selection == '2':
                    message = 'select a file to send to server:'
                    connection.sendall(message)
                elif selection == '3':
                    message = 'select a file to retrieve from server:'
                    connection.sendall(message)
                elif selection == '4':
                    message = 'select a directory to move to:'
                    connection.sendall(message)
                elif selection == '5':
                    message = 'select a directory to make:'
                    connection.sendall(message)
                else:
                    break

        finally:
            # clean up the connection
            connection.close()
