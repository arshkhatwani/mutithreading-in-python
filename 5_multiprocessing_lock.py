from multiprocessing import Value, Process, Lock
from time import sleep


def deposit(balance, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == '__main__':
    balance = Value('i', 200)
    lock = Lock()

    d = Process(target=deposit, args=(balance, lock))
    w = Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print('Balance', balance.value)
