import threading
import time
import os
from multiprocessing import Process

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = sum(range(10 ** 9))
    print(f"Total {total}")


# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
# start = time.time()
# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join() 
# end = time.time()
# print(f"Time taken {end - start:.2f}")

#Using Process
if __name__ == "__main__":
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    start = time.time()
    for process in processes:
        process.start()

    for process in processes:
        process.join() 
    end = time.time()
    print(f"Time taken {end - start:.2f}")

        