import socket 

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv.bind(('0.0.0.0', 8080))

serv.listen(5)

while True:
    conn, addr = serv.accept()
    
    from_client = ''

    while True:
        data = conn.recv(4096)
        data = data.decode()
        if not data: break
        from_client += data
        print(from_client)
        output = "I am the SERVER <br/>"
        conn.sendall(output.encode('utf-8'))

    conn.close

    print('client disconnected')
