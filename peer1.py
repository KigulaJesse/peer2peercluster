from queue import Queue
from threading import Thread
import time
import socket 

def client(out_q):
    file = 'y'
    x = 0
    while file != 'n':
        if x == 0:
            addressNum = input("Please Enter peer address: ")
            portNum = input("Please Enter peer port: ")
            x += 1
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((addressNum,int(portNum)))
        file = input("Enter new query: ")
        client.sendall(file.encode('utf-8'))
        from_peer1 = client.recv(4096)
        data = from_peer1.decode()
        if data == 'Send Blackwidow':
            print("Received Blackwidow")
        else :
            print(data)
    client.close()

def server(in_q):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(('0.0.0.0', 8081))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        while True:
            data = conn.recv(4096)
            data = data.decode()
            if not data: break
            from_peer2 = data
            if(from_peer2 == 'Spiderman'):
                output = 'Send SpiderMan'
            else:
                output = from_peer2 + " not found"
            conn.sendall(output.encode('utf-8'))
    conn.close

q = Queue()
t1 = Thread(target = server, args =(q, ))
t2 = Thread(target = client, args =(q, ))
t1.start()
t2.start()

