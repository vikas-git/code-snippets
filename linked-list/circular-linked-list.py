class Node:
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.link = None

'''
    Insertion at the beginning of the list (push)
    Insertion at the end of the list (append)
    Insertion in between the nodes
'''

class CircularLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0

    def print_list(self):
        temp = self.last.link
        if self.last is not None:
            while True:
                print(temp.data, " ")
                if temp == self.last:
                    break
                temp = temp.link
        return

    # insert in empty list
    def insert_in_empty_list(self, data):
        new_node = Node(data)
        self.last = new_node
        self.last.link = self.last
        self.size +=1
        return


    # insert at beginning of list
    def push(self, data):
        # there is no node in list
        if self.last is None:
            self.insert_in_empty_list(data)
            return

        new_node = Node(data)
        new_node.link = self.last.link
        self.last.link = new_node

        self.size +=1
        return

    # insert at end of list
    def append(self, data):
        # there is no node in list
        if self.last is None:
            self.insert_in_empty_list(data)
            return

        new_node = Node(data)
        new_node.link = self.last.link
        self.last.link = new_node
        self.last = new_node
        self.size +=1
        return


    def insert_after_node(self, x, data):
        if self.last is None:
            raise Exception("Linked List is empty")

        p = self.last.link
        while True:
            if p.data == x:
                break
            p = p.link
            if p == self.last.link:
                break

        if p == self.last.link and p.data != x:
            raise Exception("Item not found in Linked list")
        else:
            new_node = Node(data)
            new_node.link = p.link
            p.link = new_node

            if p == self.last:
                self.last = new_node
            self.size +=1
        return


    def delete_first_node(self):
        # empty list
        if self.last is None:
            raise Exception("Linked List is empty")

        # list has only one node
        if self.last == self.last.link:
            self.last = None
            self.size -= 1
            return

        self.last.link = self.last.link.link
        self.size -= 1
        return

    def delete_last_node(self):
        # empty list
        if self.last is None:
            raise Exception("Linked List is empty")

        # list has only one node
        if self.last == self.last.link:
            self.last = None
            self.size -= 1
            return

        p = self.last.link
        while p.link != self.last:
            p = p.link

        p.link = self.last.link
        self.last = p
        self.size -= 1
        return

    def delete_node_by_value(self, x):
        # empty list
        if self.last is None:
            raise Exception("Linked List is empty")

        # list has only one node
        if self.last == self.last.link and self.last.data == x:
            self.last = None
            self.size -= 1
            return

        # deletion of first node
        if self.last.link.data == x:
            self.last.link = self.last.link.link
            self.size -= 1
            return

        p = self.last.link
        while p.link != self.last.link:
            if p.link.data == x:
                break
            p = p.link
        if p.link == self.last.link:
            raise Exception(str(x)+" node not found.")
        else:
            p.link = p.link.link
            if self.last.data == x:
                self.last = p
            self.size -= 1

        return


if __name__ == "__main__":
    try:
        sll = CircularLinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        sll.append(40)

        sll.insert_after_node(10, 50)
        # sll.delete_first_node()
        # sll.delete_last_node()
        sll.delete_node_by_value(20)

        sll.print_list()
        print()
        print(sll.size)
    except Exception as e:
        print(e)