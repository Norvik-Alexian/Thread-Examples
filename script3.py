from threading import Thread
from queue import Queue


def add_value(data):
    for i in range(10):
        data.put(f'added <-> {i}')


def read_value(data):
    for i in range(10):
        print(data.get())


queue_value = Queue(15)

thread_1 = Thread(target=add_value, args=(queue_value,))
thread_2 = Thread(target=read_value, args=(queue_value,))

thread_1.start()
thread_2.start()
