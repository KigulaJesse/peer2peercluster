import time
from node import Node

def node_callback(event, main_node, connected_node, data):
    try:
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            print('Event: {} from main node {}: connected node {}: {}'.format(event, main_node.id, connected_node.id, data))

    except Exception as e:
        print(e)



node_1 = Node("127.0.0.1", 8001, id=1, callback=node_callback)
node_1.start()

file = 'y'
x = 0
while file != 'n':
    if x == 0:
        addressNum = input("Please Enter peer address: ")
        portNum = input("Please Enter peer port: ")
        x += 1
    node_1.connect_with_node('addressNum', portNum)
    file = input("Enter new query: ")
    node_1.send_to_nodes("message: hoi from node 1")
        
node_1.stop()
print('end')
