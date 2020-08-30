'''
    https://github.com/codebasics/py/blob/master/DataStructures/7_Tree/7_tree_exercise.md
'''

class CompanyTree:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.parent = None
        self.child = []

    def add_child_node(self, child):
        child.parent = self
        self.child.append(child)

    def print_tree(self, option):
        spaces = ' '* self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""

        if option == 'name':
            print(prefix + self.name)
        elif option == 'designation':
            print(prefix + self.designation)
        elif option == 'both':
            print(prefix + self.name +' ('+self.designation + ')')

        if self.child:
            for child in self.child:
                child.print_tree(option)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

def build_product_tree():
    root = CompanyTree("Nilupul", "CEO")

    cto = CompanyTree("Chinmay", "CTO")
    ih = CompanyTree("Vishwa", "Infrastructure head")

    ih.add_child_node(CompanyTree("Dhaval", "Cloud Manager"))
    ih.add_child_node(CompanyTree("Abhijit", "App Manager"))

    cto.add_child_node(ih)
    cto.add_child_node(CompanyTree("Aamir", "Application Head"))

    hr = CompanyTree("Gels", "HR Head")
    hr.add_child_node(CompanyTree("Peter", "Recuritment Manager"))
    hr.add_child_node(CompanyTree("Waqas", "Policy Manager"))

    root.add_child_node(cto)
    root.add_child_node(hr)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    # root.print_tree("name")
    # root.print_tree("designation")
    root.print_tree("both")
