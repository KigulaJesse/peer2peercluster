import time
import socket

from test import is_port_in_use 


class Peer():
    def __init__(self,peerName,peerID,maxPeers=None):
        self.peerName = peerName
        self.peerID = peerID
        if maxPeers:
            self.maxPeers = int(maxPeers)
        else:
            self.maxPeers = 2
        self.peerPort = 5000 + int(peerID)
        self.peerHost = "127.0.0.1"
        self.peers = []
        self.hashTable = {}
        self.connectToPeers()

    
    def client(self):
        print("****************************")
        print("\t" +self.peerName)
        print("****************************")

        n = -1
        while n != 4:

            try:
                print("\n****CLIENT MENU****")
                print("1. Register a File")
                print("2. Search for a File")
                print("3. Obtain a File")
                print("4. EXIT \n")

                n = input("Enter your choice: ")

                if int(n) == 1:
                    fileName = input("Enter filename with extension: ")
            
                    #Store that you have file in Hash
                    self.storeInHash(fileName,self.peerName)

                    #success message on replication
                    print("Success")

                elif int(n) == 2:
                    fileName = input("Enter the File Name to be searched: ")
                    self.peersWithFile = []
                    if fileName in self.hashTable:
                        self.peersWithFile.append(self.peerName)
                    
                    searchRequest = "s" + fileName
                    if len(self.peers) > 0:
                        for ID in self.peers:
                            peerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
                            port = 5000 + int(ID)               
                            peerSocket.connect(('127.0.0.1', port))
                            peerSocket.sendall(searchRequest.encode('utf-8'))
                            fromPeer = peerSocket.recv(4096)
                            fromPeer = fromPeer.decode()
                            if fromPeer == "found":
                                self.peersWithFile.append("peer"+str(ID))
                            peerSocket.close()
                    print(self.peersWithFile)
                    
                elif int(n) == 3:
                    obtainFileName = input("Enter the File Name:")
                    obtainPeerName = input("From where you wish to obtain " + fileName + " :")
                    
                    self.obtain(obtainFileName,obtainPeerName)
					
					
                elif int(n) == 4:
                    #replication of all in its hash table
                    print("Replication to all peers")

                else:
                    print("Please choose a correct command")
            except ValueError:
                print("\nPlease enter the correct commands")
        

    def server(self):
        peerServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peerServ.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        peerServ.bind((self.peerHost, self.peerPort))
        peerServ.listen(5)
        while True:
            conn, addr = peerServ.accept()
            while True:
                incomingRequest = conn.recv(4096)
                incomingRequest = incomingRequest.decode()
                if not incomingRequest: break
                if incomingRequest[0] == 's':
                    outGoingRequest = self.searchForResource(incomingRequest)
                else:
                    outGoingRequest = "bluh"
                conn.sendall(outGoingRequest.encode('utf-8'))
        conn.close




    def searchForResource(self, searchRequest):
        if searchRequest[1:] in self.hashTable:
            return "found"
        else:
            return "not"

    def storeInHash(self,key,value):
        self.hashTable[key] = value
    
    def connectToPeers(self):
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        x = 0
        while (x <= 3):
            checkedPort = 5000 + x
            if checkedPort == self.peerPort:
                x += 1
                continue
            checkedPortResult = is_port_in_use(checkedPort)
            if checkedPortResult:
                self.peers.append(x)
            x += 1

    def is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', port)) == 0
