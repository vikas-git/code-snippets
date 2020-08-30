

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, element):
        return self.items.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is underflow")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        print(self.items[-1])

    def size(self):
        print(len(self.items))

    def display(self):
        print(self.items)


if __name__ == "__main__":
    obj = Stack()
    while True:
        print('-'*50)
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = input("Enter the element to be pushed : ")
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