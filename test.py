import socket 


def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


# Python 3 code to demonstrate
# working of hash()

# initializing objects
str_val = 'GeeksforGeeks'

def HashFunction(Key):
    hash1 = hash(Key)
    
    
searchRequest = "s" + "then"

print(searchRequest[0])



