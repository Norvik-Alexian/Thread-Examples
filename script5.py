from time import sleep
from timeit import timeit


def sleep_calculation():
    sleep(0.5)
    print('this is message')


counter = 0
one = timeit(stmt=sleep_calculation, number=1)
counter += one
two = timeit(stmt=sleep_calculation, number=1)
counter += two
three = timeit(stmt=sleep_calculation, number=1)
counter += three

print(counter)
print(timeit(stmt=sleep_calculation, number=3))
