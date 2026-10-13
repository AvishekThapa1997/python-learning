from multiprocessing import Process,current_process
import time

def process_data():
    process = current_process().name
    print(f"{process} start processing...")
    count = 0
    for _ in range(1_00_00_00_00):
        count += 1
    print(f"{process} finished processing...")


if __name__ == "__main__":
    process_1 = Process(target=process_data, name="Process-1")
    process_2 = Process(target=process_data, name="Process-2")

    start = time.time()
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    end = time.time()
    print(f"Execution Time is {end - start:.2f}")