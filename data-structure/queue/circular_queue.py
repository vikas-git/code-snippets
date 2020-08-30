'''
    In last example(queue.py), there is an issue
    we can't use again deleted item location
    suppose we have a queue []10,20,30,40]
    and we apply dequeue operation then output will be like [None,20,30,40]
    when we add new element it add to last of the list [None,20,30,40,50]
    for this drawback we use circular queue
'''

class CircularQueue:
    def __init__(self, default_size=10):
        self.items = [None]*default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1
        return

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]

    def print_queue(self):
        print(self.items)
        return

    def resize(self, new_length):
        old_list = self.items
        self.items = [None]* new_length
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i)%len(old_list)
        self.front = 0
        return


if __name__ == "__main__":
    queue = CircularQueue(4)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.print_queue()

    # print(queue.peek())
    print(queue.dequeue())
    queue.enqueue(50)
    print(queue.peek())
    queue.print_queue()