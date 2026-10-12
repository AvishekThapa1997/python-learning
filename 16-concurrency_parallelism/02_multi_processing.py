import math
from multiprocessing import Process
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(i)
    print("Taking order completed")    

def process_data(processor):
    print("Processor", processor)
    for i in range(1,5):
        print(f"Processing data #{i}")
        time.sleep(math.prod([i,2]))
    print("Processing data completed")

if __name__ == "__main__":
    processors = [
        Process(target=process_data,args=(f"Processor ${i+1}",))
        for i in range(3)
    ]
    for processor in processors:
        processor.start()

    for processor in processors:
        processor.join()    

print("Main completed")        
