class HashTable:
    def __init__(self):
        self.Max =10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        count = 0
        for i in key:
            count += ord(i)
        return count % self.Max

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key :
            return self.arr[h][1]
        else:
            h = (h+1)%self.Max
            while self.arr[h][0] != key:
                h = (h+1)%self.Max
            return self.arr[h][1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] != None:
            count = 0
            while count<self.Max:
                h = (h + 1) % self.Max
                if self.arr[h] != None:
                    count +=1
                    continue
                elif self.arr[h] == None:
                    self.arr[h] = (key,value)

        elif self.arr[h] == None:
            self.arr[h] = (key,value)
        return

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

if __name__ == '__main__':
    h = HashTable()
    print(h.arr)
    h["march 8"] = 32
    print(h.arr)
    h["march 9"] = 40
    print(h.arr)
    h["march 10"] = 35
    print(h.arr)
    h["march 11"] = 50
    print(h.arr)
    h["march 12"] = 1
    print(h.arr)
    h["march 1"] = 32
    print(h.arr)
    h["march 2"] = 40
    print(h.arr)
    h["march 3"] = 35
    print(h.arr)
    h["march 4"] = 50
    print(h.arr)
    h["march 5"] = 1
    print(h.arr)
    h["march 6"] = 1
    print(h.arr)
    h["march 7"] = 12
    print(h.arr)

    # print(h["march 8"])
    # print(h["march 9"])
    # print(h["march 10"])
    # print(h["march 12"])
    # print(h["march 1"])
    #