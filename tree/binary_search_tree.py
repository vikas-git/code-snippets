
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        if data == self.data:
            return

        # add node in left side
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        # add node in right side
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    # also known as ASC order
    def inorder_recursive(self):
        elements = []
        # visit Left first
        if self.left:
            elements += self.left.inorder_recursive()

        # visit root
        elements.append(self.data)

        # visit Right
        if self.right:
            elements += self.right.inorder_recursive()

        return elements


    def preorder_recursive(self):
        elements = []

        # visit root
        elements.append(self.data)

        # visit Left
        if self.left:
            elements += self.left.preorder_recursive()

        # visit Right
        if self.right:
            elements += self.right.preorder_recursive()

        return elements

    def postorder_recursive(self):
        elements = []

        # visit Left
        if self.left:
            elements += self.left.postorder_recursive()

        # visit Right
        if self.right:
            elements += self.right.postorder_recursive()

        # visit root
        elements.append(self.data)

        return elements

    # search
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        sum = 0

        # visit Left
        if self.left:
            sum += self.left.calculate_sum()

        # visit Right
        if self.right:
            sum += self.right.calculate_sum()

        # visit root
        sum += self.data

        return sum

    def delete(self):
        pass

def build_bst(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 70, 23, 18, 34, 4]
    numbers_tree = build_bst(numbers)
    print(numbers_tree.inorder_recursive())
    print(numbers_tree.preorder_recursive())

    print(numbers_tree.search(20))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())