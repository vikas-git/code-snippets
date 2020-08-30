class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node

        self.rear = new_node
        self.size +=1
        return


    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        x = self.front.data
        self.front = self.front.next
        self.size -= 1
        return x

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return
        return self.front.data


    def print_queue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    queue = QueueUsingLinkedList()

    print(queue.peek())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.print_queue()
    print('')
    # print(queue.peek())
    print(queue.dequeue())
    print('')
    # queue.enqueue(50)

    # print(queue.peek())
    queue.print_queue()

