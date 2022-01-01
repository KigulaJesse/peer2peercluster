from threading import Thread
from queue import Queue
import peer

peer2 = peer.Peer(2,1,12346,'0.0.0.0')
t1 = Thread(target = peer2.server,)
t2 = Thread(target = peer2.client,)
t1.start()
t2.start()
