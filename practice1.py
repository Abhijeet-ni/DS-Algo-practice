def fib(n):
    prev, curr = 0, 1
    while prev < n:
        value = prev
        prev, curr = curr, prev + curr
        yield value


if __name__ == '__main__':
    fibonaccigenerator = fib(20)
    for i in range(1, 10, 1):
        try:
            print(next(fibonaccigenerator))
        except StopIteration:
            break
