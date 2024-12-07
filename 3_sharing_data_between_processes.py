import multiprocessing


def calc_square(numbers, result, v):
    v.value = 2.3
    for idx, n in enumerate(numbers):
        result[idx] = n * n


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)

    p1 = multiprocessing.Process(target=calc_square, args=(nums, result, v))

    p1.start()
    p1.join()

    for item in result:
        print(item)

    print(v.value)
