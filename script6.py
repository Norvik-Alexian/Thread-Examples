from threading import Thread, RLock

digit = 254
lock = RLock()


def get_perv_5():
    global digit, lock
    lock.acquire()
    if digit % 5 == 0:
        print(digit)
    else:
        digit -= 1
        get_perv_5()
    lock.release()


Thread(target=get_perv_5).start()