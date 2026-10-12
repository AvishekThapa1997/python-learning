import math
from threading import Thread
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(i)
    print("Taking order completed")    

def process_data():
    for i in range(1,4):
        print(f"Processing data #{i}")
        time.sleep(math.prod([i,2]))
    print("Processing data completed")    
                
#create threads
order_thread = Thread(target=take_orders)
process_thread = Thread(target= process_data)
order_thread.start()
process_thread.start() 

order_thread.join()
process_thread.join()
print("Main completed")