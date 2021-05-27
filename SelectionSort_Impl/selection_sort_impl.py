def find_min(element):
    min=1000000
    for i in range(len(element)):
        if element[i]<min:
            min=element[i]
    return min

if __name__=='__main__':
    element=[78,12,15,8,2,61,53,23,27]
    print(find_min(element))