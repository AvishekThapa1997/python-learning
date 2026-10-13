import threading
import time

def process_data():
    thread = threading.current_thread().name
    print(f"{thread} start processing...")
    count = 0
    for _ in range(1_00_00_00_00):
        count += 1
    print(f"{thread} finished processing...")


thread_1 = threading.Thread(target=process_data, name="Thread-1")
thread_2 = threading.Thread(target=process_data, name="Thread-2")
start = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end = time.time()

print(f"Total time taken : {end - start:.2f}")


        
