from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep

executer = ProcessPoolExecutor(max_workers=4)


def print_message():
    sleep(2)
    print('This is a message!')


# for _ in range(10):
#     executer.submit(print_message)


def calculate(number: int):
    counter = 2
    counter *= number
    return counter


output = executer.map(calculate, [i for i in range(7)])

print(list(output))