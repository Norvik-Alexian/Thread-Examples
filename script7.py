from threading import Semaphore, Thread
from time import sleep

sem_obj = Semaphore(3)


def process_request(sema):
    sema.acquire()
    print('request is processed!')
    sleep(0.5)
    sema.release()


threads = [Thread(target=process_request, args=(sem_obj,)) for _ in range(8)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()