import time
import threading


def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)


def calc_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)


numbers = [1, 2, 3, 4, 5]

start_time = time.time()

# Normal approach - functions will be executed one by one
# calc_square(numbers)
# calc_cube(numbers)

# Multithreading approach
t1 = threading.Thread(target=calc_square, args=(numbers, ))
t2 = threading.Thread(target=calc_cube, args=(numbers, ))

t1.start()
t2.start()

t1.join()
t2.join()

duration = time.time() - start_time

print(f'Execution completed in {duration} seconds')
