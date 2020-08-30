'''
    https://github.com/codebasics/py/blob/master/DataStructures/7_Tree/7_tree_exercise.md
'''


class CountryTree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = []

    def add_child_node(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self, level):
        if self.get_level() > level:
            return

        spaces = ' '* self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)

        if self.child:
            for child in self.child:
                child.print_tree(level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

def build_tree():
    root = CountryTree("Global")

    india = CountryTree("India")
    gujarat = CountryTree("Gujarat")
    gujarat.add_child_node(CountryTree("Ahmedabad"))
    gujarat.add_child_node(CountryTree("Baroda"))
    india.add_child_node(gujarat)

    karnataka = CountryTree("Karnataka")
    karnataka.add_child_node(CountryTree("Bengluru"))
    karnataka.add_child_node(CountryTree("Mysore"))
    india.add_child_node(karnataka)

    usa = CountryTree("USA")
    new_jersey = CountryTree("New Jersey")
    new_jersey.add_child_node(CountryTree("Priceton"))
    new_jersey.add_child_node(CountryTree("Trenton"))


    california = CountryTree("California")
    california.add_child_node(CountryTree("San francisco"))
    california.add_child_node(CountryTree("Mountain View"))
    california.add_child_node(CountryTree("Palo Alto"))

    usa.add_child_node(new_jersey)
    usa.add_child_node(california)


    root.add_child_node(india)
    root.add_child_node(usa)
    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree(level=0)

