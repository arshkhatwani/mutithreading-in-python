from multiprocessing import Pool
from time import time


def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum


if __name__ == '__main__':
    t1 = time()

    p = Pool()
    # p = Pool(processes=2) # can also specify processes to create
    result = p.map(f, range(100000))
    p.close()
    p.join()

    print('Pool took', time() - t1)

    t2 = time()
    s = 0
    for x in range(1000):
        s += x*x

    print('Serial processing took', time() - t2)
