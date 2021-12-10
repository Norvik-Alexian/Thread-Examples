from threading import Thread, Lock
from time import sleep

lock_obj_1 = Lock()
lock_obj_2 = Lock()


def print_thread_one(lock_obj_one, lock_obj_two):
    lock_obj_one.acquire()

    sleep(0.5)
    print('Acquired first then second')
    lock_obj_two.acquire()
    lock_obj_two.release()

    lock_obj_one.release()


def print_thread_two(lock_obj_one, lock_obj_two):
    lock_obj_two.acquire()

    lock_obj_one.acquire()
    print('Acquired second then first')
    sleep(0.2)
    lock_obj_one.release()

    lock_obj_two.release()


thread_1 = Thread(target=print_thread_one, args=(lock_obj_1, lock_obj_2))
thread_2 = Thread(target=print_thread_two, args=(lock_obj_1, lock_obj_2))

thread_1.start()
thread_2.start()
