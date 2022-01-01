import time
import socket 


class Peer():
    def __init__(self,maxpeers,myid,serverport,serverhost):
        self.maxpeers = int(maxpeers)
        self.serverport = int(serverport)
        self.serverhost = serverhost
        self.myid = myid
        self.peers = {}  # peerid ==> (host, port) mapping
 
    def client(self):
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
            print("I found something and returned")
        client.close()

    def server(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((self.serverhost, self.serverport))
        serv.listen(5)
        while True:
            conn, addr = serv.accept()
            while True:
                data = conn.recv(4096)
                data = data.decode()
                if not data: break
                from_peer2 = data
                output = "You are looking for " + from_peer2
                conn.sendall(output.encode('utf-8'))
        conn.close

    def addpeer(self,peerid,host,port):
        if peerid not in self.peers and (self.maxpeers == 0
                or len(self.peers) < self.maxpeers):
            self.peers[peerid] = (host, int(port))
            return True
        else:
            return False

    # --------------------------------------------------------------------------

