def sum(data_list):
    if len(data_list) == 1:
        return data_list[0]
    return data_list[0] + sum(data_list[1:])


def to_string(n, base):
    conver_tString = "0123456789ABCDEF"
    if n < base:
        return conver_tString[n]
    else:
        return to_string(n // base, base) + conver_tString[n % base]


def sum_list(data):
    total = 0
    for element in data:
        if type(element) == list:
            total = total + sum_list(element)
        else:
            total = total + element
    return total


def factorial(val):
    if val <= 1:
        return 1
    return val * factorial(val - 1)


def fibonacci(val):
    if val == 1 or val == 2:
        return 1
    else:
        return fibonacci(val - 1) + fibonacci(val - 2)


def sum_of_digit(val):
    if val // 10 == 0:
        return val
    else:
        return val % 10 + sum_of_digit(val // 10)


def sum_of_even(val):
    if val == 0:
        return val
    else:
        return val + sum_of_even(val - 2)


def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * pow(a, b - 1)


if __name__ == '__main__':
    # print(sum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
    # print(to_string(2835,16))
    # print(sum_list([1, 2, [3,4], [5,6]]))
    # print(factorial(5))
    # print(fibonacci(7))
    # print(sum_of_digit(45))
    # print(sum_of_even(10))
    print(pow(2, 3))
