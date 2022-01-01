from threading import Thread
from queue import Queue
import peer

peer1 = peer.Peer(2,0,12345,'0.0.0.0')
q = Queue()
t1 = Thread(target = peer1.server, args=( ))
t2 = Thread(target = peer1.client, args=( ))
t1.start()
t2.start()
