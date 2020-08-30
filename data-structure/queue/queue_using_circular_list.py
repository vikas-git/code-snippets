class Node:
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.link = None


class QueueUsingCircularList:
    def __init__(self):
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        # there is no node in list
        if self.rear is None:
            self.insert_in_empty_list(data)
            return

        new_node = Node(data)
        new_node.link = self.rear.link
        self.rear.link = new_node
        self.rear = new_node
        self.size +=1
        return

    # insert in empty list
    def insert_in_empty_list(self, data):
        new_node = Node(data)
        self.rear = new_node
        self.rear.link = self.rear
        self.size +=1
        return

    def dequeue(self):
        # empty list
        if self.rear is None:
            raise Exception("Queue is empty")

        # list has only one node
        if self.rear == self.rear.link:
            temp = self.rear
            self.rear = None
        else:
            temp = self.rear.link
            self.rear.link = self.rear.link.link

        self.size -= 1
        return temp.data

    def print_list(self):
        temp = self.rear.link
        if self.rear is not None:
            while True:
                print(temp.data, " ")
                if temp == self.rear:
                    break
                temp = temp.link
        return

    def peek(self):
        if self.rear is None:
            raise Exception("Queue is empty.")
        return self.rear.link.data

#####################################################

if __name__ == "__main__":
    try:
        sll = QueueUsingCircularList()
        sll.enqueue(10)
        sll.enqueue(20)
        sll.enqueue(30)
        sll.enqueue(40)

        sll.print_list()
        print('')

        sll.dequeue()
        print('')
        sll.print_list()
        
        print(sll.peek())
        # sll.delete_node_by_value(20)

        # sll.print_list()
        # print()
        # print(sll.size)
    except Exception as e:
        print(e)