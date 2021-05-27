import time

def linear_search(number_list, value_to_search):
    for index,element in enumerate(number_list):
        if element == value_to_search:
            return index
    return -1

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result

    return wrapper

if __name__=='__main__':
    list=[1,4,6,9,10,5,7]
    index = linear_search(list, 5)
    print("the number 15 is in : {} index".format(index ))