from queue import Queue
from threading import Thread
import time
import socket 

def client(out_q):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0',8082))
    file = 'y'
    while file != 'n':
        file = input("Enter new query: ")
        client.sendall(file.encode('utf-8'))
        from_server = client.recv(4096)
        data = from_server.decode()
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
                print(from_peer2)
                output = 'Send SpiderMan'
            else:
                output = from_peer2 + " not found"
            conn.sendall(output.encode('utf-8'))
    conn.close

q = Queue()
t1 = Thread(target = server, args =(q, ))
#t2 = Thread(target = client, args =(q, ))
t1.start()
#t2.start()

