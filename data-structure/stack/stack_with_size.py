'''
    without list functions
'''
class Stack:
    def __init__(self, max_items):
        self.max_items = max_items
        self.items = [None]*self.max_items
        self.count = 0

    def size(self):
        print(self.count)

    def is_empty(self):
        return self.count == 0

    def is_overflow(self):
        return len(self.items) == self.count

    def display(self):
        print(self.items)

    def push(self, item):
        if self.is_overflow():
            raise Exception("Stack is Overflow")
        self.items[self.count] = item
        self.count += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        print(self.items[self.count-1])

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is underflow")

        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        print(x)

'''
if __name__ == "__main__":
    obj = Stack(3)
    while True:
        print('-'*100)
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = input("Enter the element to be pushed : ")
            print(x)
            obj.push(x)
        elif choice == 2:
            obj.pop()
        elif choice == 3:
            obj.peek()
        elif choice == 4:
            obj.size()
        elif choice == 5:
            obj.display()
        elif choice == 6:
            break
        else:
            print("Wrong choice")
'''
# ---------------------------------------------------------------------

'''
    With List inbulit functions
'''

class StackWithInbuiltFunction:
    def __init__(self, max_items):
        self.max_items = max_items
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def is_overflow(self):
        return len(self.items) == self.max_items

    def display(self):
        print(self.items)

    def push(self, item):
        if self.is_overflow():
            raise Exception("Stack is Overflow")
        self.items.append(item)

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        print(self.items[-1])

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is underflow")

        x = self.items.pop()
        print(x)

if __name__ == "__main__":
    obj = StackWithInbuiltFunction(3)
    while True:
        print('-'*100)
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = input("Enter the element to be pushed : ")
            print(x)
            obj.push(x)
        elif choice == 2:
            obj.pop()
        elif choice == 3:
            obj.peek()
        elif choice == 4:
            print(obj.size())
        elif choice == 5:
            obj.display()
        elif choice == 6:
            break
        else:
            print("Wrong choice")