import socket
import ssl
import subprocess
import sys

# get the hostname
host = socket.gethostname()
port = int(sys.argv[1]) # initiate port no above 1024

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("/Users/dimplesingh/projects/Documents/playground-python/Computer_security/ssl_files/selfsigned.crt", "/Users/dimplesingh/projects/Documents/playground-python/Computer_security/ssl_files/private.key")

with socket.socket() as server_socket:  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    with context.wrap_socket(server_socket, server_side=True) as sock:

        conn, address = sock.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(2048).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            if str(data) == 'pwd':
                sent_data = subprocess.run(["powershell", "pwd"], capture_output=True).stdout
            elif str(data) == 'ls':
                sent_data = subprocess.run(["powershell", "ls"], capture_output=True).stdout
            else:
                sent_data = bytes("Invalid Command", 'utf-8')
            conn.send(sent_data)  # send data to the client

        conn.close()

# conn.close()  # close the connection
