import multiprocessing

from multiprocessing import Process
from time import sleep

print(multiprocessing.cpu_count())
x = 0


def print_process():
    global x
    for _ in range(10):
        sleep(0.2)
        x += 3
    print(x)


process_one = Process(target=print_process)
process_two = Process(target=print_process)
process_three = Process(target=print_process)


process_one.start()
process_two.start()
process_three.start()

process_one.join()
process_two.join()
process_three.join()