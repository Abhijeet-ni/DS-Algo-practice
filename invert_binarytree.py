# A node contains the value, left and right pointers
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def invert(node):
    if (node == None):
        return

    else:
        temp = node

        # recursive calls
        invert(node.left)
        invert(node.right)

        # swap the pointers in this node
        temp = node.left
        node.left = node.right
        node.right = temp

    # print InOrder binary tree traversal.


def print_tree(node):
    if (node == None):
        return

    print_tree(node.left)
    print(node.data,end=" ")
    print_tree(node.right)

root = newNode(2)
root.left = newNode(1)
root.right = newNode(4)
root.right.left = newNode(3)
root.right.right = newNode(5)

# Print inorder traversal of the input tree
print("Inorder traversal of the constructed tree is")
print(root)
print_tree(root)

# Convert tree to its mirror
invert(root)

# Print inorder traversal of the mirror tree
print("\nInorder traversal of the mirror treeis ")
print_tree(root)