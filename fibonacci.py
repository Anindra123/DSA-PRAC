def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def memofibonacci(n, list: dict):
    if n < 2:
        return n
    else:
        if list.get(n) is None:
            list[n] = memofibonacci(n-1, list) + memofibonacci(n-2, list)
        return list[n]


def main():
    l = {}
    print(memofibonacci(35, l))
    print(fibonacci(35))


if __name__ == '__main__':
    main()
