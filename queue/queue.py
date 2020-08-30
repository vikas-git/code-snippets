'''
    In last example (queue_using_list.py), there was an issue with dequeue operation.
    because when we dequeue an element from queue it shift all element from right to left (internally).

    for remove this drawback we use given way

'''

class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return len(self.items) == self.front

    def enqueue(self, element):
        return self.items.append(element)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]

    def print_queue(self):
        print(self.items)


if __name__ == "__main__":
    queue = Queue()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()

    print(queue.peek())
    queue.dequeue()
    queue.print_queue()