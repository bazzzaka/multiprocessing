import time
import threading


def data_daemon(data):
    for _ in range(5):
        print(f'[{threading.currentThread().name}] - {data}')
        time.sleep(1)


thr = threading.Thread(target=data_daemon, args=(str(time.time()),))
thr.setDaemon(True)
thr.start()

print('finish')