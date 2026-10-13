import threading
import time
import requests

url = "https://httpbin.org/image"
image_formats = ["png","jpeg", "webp"]
def download_image(*format):
    print(f"Starting downloading image {format} with thread {threading.current_thread().name}")
    download_url = f"{url}/{format}"
    resp = requests.get(download_url)
    print(f"Finished download from {url}, size= {len(resp.content)}")


threads = [threading.Thread(target=download_image,name=format, args=(format,)) for format in image_formats]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()    
