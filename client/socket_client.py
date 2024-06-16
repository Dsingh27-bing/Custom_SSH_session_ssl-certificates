import socket
import ssl
import sys


context = ssl._create_unverified_context()
context.load_verify_locations("/Users/dimplesingh/projects/Documents/playground-python/Computer_security/ssl_files/selfsigned.crt")

host = sys.argv[1]  # as both code is running on same pc
port = int(sys.argv[2]) # socket server port number

# client_socket = socket.socket()  # instantiate
# client_socket.connect((host, port))  # connect to the server

with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as client_socket:

        message = input("ssh > ")  # take input

        while message.lower().strip() != 'exit':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(2048).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal
            # subprocess.run(["powershell", "pwd"], shell=True)

            message = input("ssh > ")  # again take input

        client_socket.close()  # close the connection
