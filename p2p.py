


class P2pCluster:
    def __init__( self, maxpeers, serverport, myid=None, serverhost = None ):
        self.debug = 0

        self.maxpeers = int(maxpeers)
        self.serverport = int(serverport)

            # If not supplied, the host name/IP address will be determined
        # by attempting to connect to an Internet host like Google.
        if serverhost: self.serverhost = serverhost
        else: self.__initserverhost()

            # If not supplied, the peer id will be composed of the host address
            # and port number
        if myid: self.myid = myid
        else: self.myid = '%s:%d' % (self.serverhost, self.serverport)

            # list (dictionary/hash table) of known peers
        self.peers = {}  

            # used to stop the main loop
        self.shutdown = False  

        self.handlers = {}
        self.router = None
        # end constructor