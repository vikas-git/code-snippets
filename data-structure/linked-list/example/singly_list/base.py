
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class  SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            next = self.head
            while next.next is not None:
                next = next.next

            next.next = node
        return

    def print_list(self):
        if self.head is not None:
            next = self.head
            while next is not None:
                print(next.data)
                next = next.next

