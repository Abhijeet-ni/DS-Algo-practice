class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  #node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        element = []

        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

        return element

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        element = []

        if self.left:
            element.append(self.left.calculate_sum())

        element.append(self.data)

        if self.right:
            element.append(self.right.calculate_sum())

        return sum(element)

    def post_order_traversal(self):
        element = []

        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element

    def pre_order_traversal(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            # used min value from rignt side METHOD-1
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            # used min value from rignt side METHOD-2
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self



def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    # print("post order traversal gives this sorted list:", numbers_tree.post_order_traversal())
    # print("pre order traversal gives this sorted list:", numbers_tree.pre_order_traversal())
    # print(numbers_tree.search(1000))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    print(numbers_tree.delete(20))
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
