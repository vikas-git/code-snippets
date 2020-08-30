'''
    Insertion type:
        Beginning of linked list (Push)
        Ending of linked list (Append)
        After certain element of linked list
        Before certain element of linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=", ")
            temp = temp.next


    def push(self, data):
        # Allocate the Node
        new_node = Node(data)
        # Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # move the head to point to the new node
        self.head = new_node
        self.size += 1
        return

    def append(self, data):
        new_node = Node(data)
        new_node.next = None

        last = self.head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last
        self.size += 1
        return

    def insert_after(self, x, data):
        if self.head is None:
            raise Exception("Linked List is empty")

        last = self.head
        while last is not None:
            if last.data == x:
                break
            last = last.next
        if last is None:
            raise Exception("Item not found in Linked list")

        new_node = Node(data)
        new_node.prev = last
        new_node.next = last.next
        if last.next is not None:
            last.next.prev = new_node
        last.next = new_node
        self.size += 1
        return


    def insert_before(self, x, data):
        if self.head is None:
            raise Exception("Linked List is empty")

        # if first node match
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return

        last = self.head
        while last is not None:
            if last.data == x:
                break
            last = last.next

        if last is None:
            raise Exception("Item not found in Linked list")

        new_node = Node(data)
        new_node.prev = last.prev
        new_node.next = last
        last.prev.next = new_node
        last.prev = new_node
        self.size += 1
        return

    '''
        Delete from DLL programs
    '''
    def delete_first_node(self):
        # if list have no items
        if self.head is None:
            raise Exception("Linked List is empty")

        # if list only have one element
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return

    def delete_last_node(self):
        # if list have no items
        if self.head is None:
            raise Exception("Linked List is empty")

        # if list only have one element
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        last = self.head
        while last.next != None:
            last = last.next
        last.prev.next = None
        self.size -= 1
        return


    def delete_node(self, x):
        if self.head is None:
            raise Exception("Linked List is empty")

        # if list only have one element
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
                self.size -= 1
            else:
                raise Exception(str(x)+" node not found.")
            return

        # deletion of first node
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        last = self.head.next
        while last.next is not None:
            if last.data == x:
                break
            last = last.next

        # node to be deleted is in between
        if last.next is not None:
            last.prev.next = last.next
            last.next.prev = last.prev
            self.size -= 1
        else:
            if last.data == x:
                last.prev.next = None
                self.size -= 1
            else:
                raise Exception(str(x)+" node not found.")

        return

    def reverse(self):
        if self.head is None:
            return

        p1 = self.head
        p2 = self.head.next
        p1.next = None
        p1.prev = p2

        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev

        self.head = p1

if __name__ == "__main__":
    try:
        dll = DoublyLinkedList()
        dll.push(10)
        dll.push('a')
        dll.push('b')
        dll.push(20)

        # dll.append(21)
        # dll.append(22)
        # dll.append(23)
        # dll.insert_after(10, 21)
        # dll.insert_before(10, 2111)

        dll.print_list()

        # dll.delete_first_node()
        # dll.delete_last_node()
        # dll.delete_node(10)
        print()
        print(dll.size)
        dll.reverse()
        dll.print_list()
    except Exception as e:
        print(e)