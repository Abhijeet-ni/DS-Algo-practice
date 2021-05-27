from Tools.scripts.dutree import display


def reverse(head):
    if head.next is None or head is None:
        return head

    list_to_do = head.next
    reverse_list = head
    reverse_list.next = None

    while list_to_do != None:
        temp = list_to_do
        list_to_do = list_to_do.next

        temp.next = reverse_list
        reverse_list = temp

    return reverse_list


class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

class LinkedList(object):
    def __init__(self, sequence):
        self.head = Node(sequence[0])
        current = self.head
        for item in sequence[1:]:
            current.next = Node(item)
            current = current.next

# class linklist:
#     def __init__(self):
#         self.head = None
#
#     def insert(self,data):
#         newNode = Node(data)
#         if(self.head):
#             current = self.head
#             while(current.next):
#                 current = current.next
#             current.next = newNode
#         else:
#             self.head = newNode
#
#     def display(self):
#         current = self.head
#         while(current):
#             print(current.data)
#             current=current.next
#
# linkl = linklist()
# l= [7, 14, 21, 28]
# for i in l:
#     linkl.insert(i)
# print("Original: ",end="")
# linkl.display()
# list_head = reverse(linkl.head)
# print("After Reverse: ", end="")
# linkl.display()


list_head = LinkedList([7, 14, 21, 28])
print ("Original: ", end="")
print(list_head)
list_head = reverse(list_head)
print("After Reverse: ", end="")
print(list_head)

