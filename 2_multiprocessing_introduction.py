import time
import multiprocessing

square_result = []


def calc_square(numbers):
    global square_result
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)
        square_result.append(n*n)


def calc_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=calc_square, args=(numbers,))
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))

    p1.start()
    p2.start()

    print('Done', square_result)
