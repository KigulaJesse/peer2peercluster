import time
from node import Node

def node_callback(event, main_node, connected_node, data):
    try:
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            print('Event: {} from main node {}: connected node {}: {}'.format(event, main_node.id, connected_node.id, data))

    except Exception as e:
        print(e)


node_2 = Node("127.0.0.1", 8002, id=2, callback=node_callback)
time.sleep(1)

node_2.start()
time.sleep(15)

node_2.send_to_nodes("message: Hello from node 2")
time.sleep(5)

node_2.stop()
print('end')
