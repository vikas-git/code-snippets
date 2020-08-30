class Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = []

    def add_child_node(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self):
        spaces = ' '* self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.child:
            for child in self.child:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

def build_product_tree():
    root = Tree("Electronics")

    laptop = Tree("Laptop")
    laptop.add_child_node(Tree('Mac'))
    laptop.add_child_node(Tree('Surface'))
    laptop.add_child_node(Tree('Thinkpad'))

    cellphone = Tree("Cell Phone")
    cellphone.add_child_node(Tree("Iphone"))
    cellphone.add_child_node(Tree("MI"))
    cellphone.add_child_node(Tree("Google Pixel"))

    tv = Tree("TV")
    tv.add_child_node(Tree("Samsung"))
    tv.add_child_node(Tree("Sansui"))
    tv.add_child_node(Tree("LG"))

    root.add_child_node(laptop)
    root.add_child_node(cellphone)
    root.add_child_node(tv)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()