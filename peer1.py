from threading import Thread
from queue import Queue
import peer
import sys

peer1 = peer.Peer(sys.argv[1],sys.argv[1][-1])

t1 = Thread(target = peer1.server, args=( ))
t2 = Thread(target = peer1.client, args=( ))

t1.start()
t2.start()
