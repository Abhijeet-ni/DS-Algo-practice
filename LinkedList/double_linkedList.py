class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class double_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        node = Node(data, None, None)
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node
        node.prev = itr
        return

    def insert_a_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        return

    def print_forward(self):
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

    # This method prints list in forward direction. Use node.next

    def print_backward(self):
        if self.head is None:
            print("LinkList is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    # Print linked list in reverse direction. Use node.prev for this.


if __name__ == '__main__':
    ll = double_linked_list()
    ll.insert_a_list(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
