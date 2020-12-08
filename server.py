import socket
 
HOST, PORT = '', 9090
 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)

while True:
    try:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print(request)
        if not request:
            continue
        filename = request.split()[1] #filename = /test.html
        f = open(filename[1:],encoding="utf-8") #f = test.html
        outputRequest = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'
     
        client_connection.sendall(header.encode())

        for i in range(0,len(outputRequest)):
            client_connection.sendall(outputRequest[i].encode())
        client_connection.close()
    except IOError:
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        client_connection.sendall(header.encode())
        client_connection.close()

# http://localhost:8080/test.html