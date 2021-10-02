'''
    topic: Singly-Linked-list
    Ref:
        GeeksforGeeks
        and
        https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/
'''

# class for create new Node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # insert a new node at the beginning
    def push(self, data):
        # allocate the node and put in the data
        new_node = Node(data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node
        self.size += 1
        return

    # insert a new node at the end of list
    def append(self, data):
        # allocate the node and put in the data
        new_node = Node(data)

        # if list is empty then make new node as head
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        # otherwise traverse list and reach last element of list
        last = self.head
        while last.next:
            last = last.next
        # Change the next of last node
        last.next = new_node
        self.size += 1
        return

    # insert after given element
    def insert_after(self, x, data):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Item not exist in list")
            return

        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node
        self.size += 1
        return


    # insert after given element
    def insert_before(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

        if n.next is None:
            print("element not exist in list")
            return

        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node
        self.size += 1
        return

    # Delete
    def delete_node_by_value(self, key):
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                self.size -= 1
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            print("The element not present in list.")
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
        self.size -= 1
        return


    # delete node from start
    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        self.head = self.head.next
        self.size -= 1
        return

    # delete node from end
    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.size -= 1
        return

    def delete_list(self):
        temp = self.head
        while temp:
            next_node = temp.next
            del temp.data
            temp = next_node
            self.size -= 1
        return


    def delete_element_by_position(self, position):
        '''
            position : 1
            Input : 8 3 4 5
            output : 8 4 5
        '''
        if self.head is None:
            print("The list has no element to delete")
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            self.size -= 1
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        # If position is more than number of nodes
        if temp is None or temp.next is None:
            raise Exception("Position not found")

        new_next = temp.next.next
        temp.next = new_next
        self.size -= 1
        return


    '''
        Reversing a Linked List
    '''
    def reverse_list(self):
        if self.size == 0:
            print("This list has no element.")
            return
        if self.size > 1:
            prev = None
            n = self.head

            while n:
                next = n.next
                n.next = prev
                prev = n
                n = next
            self.head = prev
        return


    def get_count(self):
        temp = self.head
        count = 0

        while temp:
            count +=1
            temp = temp.next
        return count

    def get_count_recursive(self, node):
        if not node:
            return 0
        else:
            return 1+ self.get_count_recursive(node.next)

    def call_count_recursive(self):
        return self.get_count_recursive(self.head)




if __name__ == "__main__":
    obj = SinglyLinkedList()
    obj.push(10)
    obj.push(20)
    obj.append(25)
    obj.insert_after(10, 11)
    obj.insert_before(10, 9)

    obj.print_list()
    print('*'*50)
    print(obj.get_count())
    # obj.reverse_list()
    # obj.delete_element_by_position(5)
    # obj.print_list()
    # obj.delete_at_end()
    # obj.reverse_list()
    # obj.print_list()
