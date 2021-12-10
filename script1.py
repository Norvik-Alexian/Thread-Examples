from threading import Thread, Lock


def print_fifty_times():
    for _ in range(50):
        print('hello')


def print_thirty_times():
    for _ in range(30):
        print('this is 30 method')


child_thread = Thread(target=print_fifty_times, daemon=True)
child_thread.start()

second_child_thread = Thread(target=print_thirty_times, daemon=True)
second_child_thread.start()

child_thread.join()
second_child_thread.join()

print('Main thread is executed')


class NewThread(Thread):
    def __init__(self, message: str, time_count: int):
        Thread.__init__(self)
        self.message = message
        self.time_count = time_count

    def run(self) -> None:
        for _ in range(self.time_count):
            print(self.message)


third_child = NewThread('this is third child thread', 20)
third_child.start()

forth_child = NewThread('This is forth child thread', 30)
forth_child.start()

print('Action performed by the main thread')


deposit = 30400


def add_deposit(lock_obj):
    global deposit

    for _ in range(1000):
        lock_obj.acquire()
        deposit += 1
        lock_obj.release()


def substract_deposit(lock_obj):
    global deposit
    lock_obj.acquire()

    for _ in range(1000):
        deposit -= 1

    lock_obj.release()


lock_obj = Lock()
lock_obj.acquire()
lock_obj.release()

thread_1 = Thread(target=add_deposit, args=(lock_obj,))
thread_2 = Thread(target=substract_deposit, args=(lock_obj,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
lock_obj.acquire()
