import threading
import time


def process_data():
    print("Processing data")
    time.sleep(5)
    print("Processing complete")


def get_data():
    print("Getting data")
    time.sleep(10)
    print('Data Received')

thread_1 = threading.Thread(target=get_data)
thread_2 = threading.Thread(target=process_data)


start = time.time()
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end = time.time()

print(f"Executoon Time {end - start:.2f}")
