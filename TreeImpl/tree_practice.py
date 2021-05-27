class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,key,level):
        if key == "name":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree("name",level)

        elif key == "designation":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree("designation")

        elif key == "both" :
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name + " " + "("+self.designation+")")
            if self.children:
                for child in self.children:
                    child.print_tree("both")

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_management_tree():
    root = TreeNode("Nilupal","CEO")

    cto = TreeNode("Chinmay","CTO")

    infrahead = TreeNode("Vishwal","Infrastructure Head")
    infrahead.add_child(TreeNode("Dhaval","Cloud Manager"))
    infrahead.add_child(TreeNode("Abhijit","App Manager"))

    cto.add_child(infrahead)
    cto.add_child(TreeNode("Aamir","Application Head"))

    hr = TreeNode("Gels","HR Head")
    hr.add_child(TreeNode("Peter","Recuitment Manager"))
    hr.add_child(TreeNode("Waqas","Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)

    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    # root_node.print_tree("designation")  # prints only designation hierarchy
    # root_node.print_tree("both")  # prints both (name and designation) hierarchy
