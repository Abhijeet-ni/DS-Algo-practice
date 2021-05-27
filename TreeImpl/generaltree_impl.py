
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parents = None

    def get_level(self):
        level = 0
        p = self.parents
        while p:
            level += 1
            p = p.parents

        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__"
        print(prefix + self.data)
        if self.child:
            for child in self.child:
                child.print_tree()


    def add_child(self, child):
        child.parents = self
        self.child.append(child)


def build_product_tree():
    root = TreeNode("Electronic")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("lenovo"))
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Hp"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Mi"))
    cellphone.add_child(TreeNode("Apple"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # return root

    root.print_tree()


if __name__ == '__main__':
    product_root = build_product_tree()
    # product_root.print_tree()
    pass
