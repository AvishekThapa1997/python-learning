from multiprocessing import Process,Queue

def process_data(queue):
    queue.put(10)


if __name__ == "__main__":
    queue = Queue()
    process = Process(target=process_data, args=(queue,))
    process.start()
    process.join()
    print(queue.get())   