import threading
import time


def monitor_system_health():
    while True:
        print("Monitoring health system")
        time.sleep(2)

# Daemon thread are threas which shuts down when main thread shuts down
threading.Thread(target=monitor_system_health, daemon=False).start()      