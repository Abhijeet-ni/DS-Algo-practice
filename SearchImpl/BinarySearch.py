# from SearchImpl.linearSearch import linear_search
from SearchImpl.linearSearch import time_it
index1 = []
@time_it
def linear_search(number_list, value_to_search):
    index1 = []
    for index,element in enumerate(number_list):
        if element == value_to_search:
            index1.append(index)
    if index1:
        return index1
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    start = 0
    end = len(numbers_list)-1
    mid = 0
    if start == end:
        return -1

    while start <= end:

        mid = (start+end)//2
        mid_value = numbers_list[mid]
        if number_to_find==mid_value:
            return mid
        elif number_to_find > mid_value:
            start=mid+1
        else:
            end = mid-1

    return -1

@time_it
def binary_recursion(numbers_list, number_to_find, start, end):
    if start > end:
        return -1

    mid_index = (start + end)//2

    if mid_index > len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        start = mid_index + 1
    else:
        end = mid_number -1

    return binary_recursion(numbers_list, number_to_find, start, end)


if __name__=='__main__':
    list = [i for i in range(100001)]
    list1 = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    index = linear_search(list1, 15)
    index1  = binary_recursion(list1,15,0,len(list1)-1)
    print("the number 15 is in : {} index".format(index ))
    print("the number 15 is in : {} index".format(index1))