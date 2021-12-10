from threading import Thread
from time import sleep
from random import randint


def add():
    for i in range(5):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        add_output = number_1 + number_2
        print(f'number one: {number_1}')
        print(f'number two: {number_2}')
        print(f'\nsummation result: {add_output}\n')


def print_current_seconds():
    current_second = 0

    while True:
        sleep(1)
        current_second += 1
        print(f'\t\t\tcurrent second: {current_second}')


thread_1 = Thread(target=add, daemon=True)
thread_2 = Thread(target=print_current_seconds)

thread_1.start()
thread_2.start()

