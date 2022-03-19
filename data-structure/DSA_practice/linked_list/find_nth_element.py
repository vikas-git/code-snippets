
# Write a function to get Nth node in a Linked List
# Time Complexity: O(n) 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            while next_node.next is not None:
                next_node = next_node.next

            next_node.next = new_node
        return

    
    def print_list(self):
        next_node = self.head
        while next_node is not None:
            print(next_node.data)
            next_node = next_node.next

    #iterate function
    def findNth(self, nth_index):
        index = 0
        next_node = self.head
        while next_node is not None:
            if index == nth_index:
                return next_node.data
            
            next_node = next_node.next
            index += 1
        return "NO index exist"


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)

ll.print_list()
print('*'*100)
print ( ll.findNth(5) )

