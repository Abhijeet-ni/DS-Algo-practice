class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node
        return

    def insert_a_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        return

    def print(self):
        if self.head is None:
            print("LinkList is empty")
            return

        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + "-->"
            itr = itr.next
        print(lstr)
        return

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            node = Node(data, self.head)
            self.head = node
            return

        itr = self.head
        node = Node(data, None)
        for i in range(index - 2):
            itr = itr.next
        node.next = itr.next
        itr.next = node
        return

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head.next = self.head.next.next
            return

        itr = self.head
        for i in range(index):
            itr = itr.next
        itr.next = itr.next.next
        return

        pass

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return

        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next)
            self.head.next = node
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            else:
                itr = itr.next
        return

    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next
        return

    def reverse(self):
        if self.head.next is None or self.head is None:
            return self.head

        itr = self.head.next
        reverse_list = self.head
        reverse_list.next = None

        itrstr = ""
        while itr:
            temp = itr
            itr = itr.next
            temp.next = reverse_list
            reverse_list = temp

        itr = reverse_list
        while itr:
            itrstr += str(itr.data) + "-->"
            itr = itr.next
        print(itrstr)
        return


# Remove first node that contains data
if __name__ == '__main__':
    # ll = linked_list()
    # # ll.insert_at_end(30)
    # # ll.insert_at_end(20)
    # # ll.insert_at_end(55)
    # ll.insert_a_list([20, 12, 2, 35, 45, 55])
    # ll.print()
    # ll.insert_at(1, 3)
    # ll.print()
    # ll.insert_after_value(20,100)
    # ll.print()
    # ll.remove_by_value(12)
    # ll.print()
    # print(ll.get_length())

    ll = linked_list()
    ll.insert_a_list(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.reverse()
    # ll.insert_after_value("mango", "apple")  # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.print()
    # ll.remove_by_value("mango")
    # ll.print()
    # ll.remove_by_value("apple")
    # ll.print()
    # ll.remove_by_value("grapes")
    # ll.print()
