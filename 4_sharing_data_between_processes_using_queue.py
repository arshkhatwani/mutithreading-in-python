import multiprocessing
import time


def calc_square(numbers, q):
    for idx, n in enumerate(numbers):
        time.sleep(0.2)
        q.put(n * n)


def calc_cube(numbers, q):
    for idx, n in enumerate(numbers):
        q.put(n * n * n)


if __name__ == '__main__':
    nums = [1, 2, 3]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=calc_square, args=(nums, q))
    p2 = multiprocessing.Process(target=calc_cube, args=(nums, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while q.empty() is False:
        print(q.get())
