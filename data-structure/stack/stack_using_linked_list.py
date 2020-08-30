'''
    Stack is work on FIFO term.
    we can choose any side for push and pop opertions
    If I choose last node for push and pop so the time complexity will be O(n)
    But if I choose first node for push and pop so the time complexity will be constant O(1).
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.head = None


    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        if self.head is None:
            print("The stack has no element to delete")
            return
        pop_node = self.head.data
        self.head = self.head.next
        return pop_node

    def peek(self):
        if self.head is None:
            print("The stack is empty")
            return
        print(self.head.data)
        return

if __name__ == "__main__":
    stack = StackUsingLinkedList()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()

    pop_node = stack.pop()
    stack.peek()
