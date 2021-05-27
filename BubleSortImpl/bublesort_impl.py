from BubleSortImpl.bs_time_it import time_it

@time_it
def buble_sort(element,key):
    swap = False
    for i in range(len(element)-1):
        for j in range(len(element)-1-i):
            if element[j][key] > element[j + 1][key]:
                max = element[j + 1]
                element[j + 1] = element[j]
                element[j] = max
                swap = True
        if swap == False:
            break

if __name__=='__main__':
    # element = [5,9,2,1,67,34,88,34]
    # element = [1,2,3]
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    buble_sort(elements, key="name")
    print(elements)