class HashTable:
    def __init__(self):
        self.Max =10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        count = 0
        for i in key:
            count += ord(i)
        return count % self.Max

    def __getitem__(self, item):
        h = self.get_hash(item)
        for i in self.arr[h]:
            if i[0]==item:
                return i[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found = True

        if not found:
            self.arr[h].append((key,value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print("del",index)
                del self.arr[h][index]


if __name__=='__main__':
    h = HashTable()
    h["march 6"] = 310
    # h["march 7"] = 320
    # h["march 8"] = 330
    # h["march 9"] = 340
    # h["march 10"] = 350
    h["march 17"] = 360
    print(h.arr)
    print(h["march 6"])
    print(h["march 17"])
    h["march 17"] = 1000
    print(h.arr)
    # del h["march 17"]
    # print(h.arr)