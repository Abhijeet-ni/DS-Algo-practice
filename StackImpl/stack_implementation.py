#stack implementation using list
# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

"""Disadvantage of list is that due to its dynamic allocation"""

#implement stack using dqueue in collection module

# from collections import deque
# stack = deque()
# stack.append('https://www.cnn.com/')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')
#
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def reverse_string(self,val):
        for i in val:
            self.push(i)
        st = ""
        for i in range(len(val)):
            st+=self.pop()

        return st

    def is_balanced(self,val):
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        for i in val:
            if i in open_list:
                self.push(i)
            elif i in close_list:
                index = close_list.index(i)
                if (self.size()>0 and open_list[index]==self.peek()):
                    self.pop()

        if self.is_empty():
            return True
        else:
            return False


if __name__ == '__main__':
    s = Stack()
    # s.push('https://www.cnn.com/')
    # s.push('https://www.cnn.com/world')
    # s.push('https://www.cnn.com/india')
    # s.push('https://www.cnn.com/china')
    #
    # print(s.is_empty())
    # print(s.size())
    # print(s.peek())
    # print(s.pop())
    # print(s.peek())
    # print(s.pop())
    # print(s.peek())
    # print(s.pop())
    # print(s.pop())
    # print(s.is_empty())
    # print(s.reverse_string("We will conquere COVID-19") == "91-DIVOC ereuqnoc lliw eW")
    # print(s.is_empty())

    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}"))