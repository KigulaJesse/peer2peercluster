import time
from threading import Thread

def listen(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

def askinput(n):
    file = 'y'
    while file != 'n':
        file = input("Enter query: ")
        print(file)
    
t = Thread(target = listen, args =(5,), daemon=True)
t.start()

x = Thread(target = askinput, args = (20,))
x.start()












"""if t.is_alive():
    print('still running')
else:
    print('Completedclea')"""