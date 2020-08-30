class QueueUsingList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, element):
        return self.items.append(element)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def print_queue(self):
        print(self.items)


if __name__ == "__main__":
    queue = QueueUsingList()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()

    print(queue.peek())
    queue.dequeue()
    queue.print_queue()