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


def is_valid(expression):
    st = Stack()
    for ch in expression:
        if ch in '({[':
            st.push(ch)
        elif ch in ')}]':
            if st.is_empty():
                print("Right parentheses are more than left parentheses")
                return False
            else:
                char = st.pop()
                if not match_parentheses(char, ch):
                    print("Mismatch parentheses are "+char+" and "+ch)
                    return False

    if st.is_empty():
        print("parentheses Balanced")
        return True
    else:
        print("Left parentheses are more than Right parentheses")
        return False


def match_parentheses(left, right):
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    if left == '(' and right == ')':
        return True
    return False

if __name__ == "__main__":
    '''
        test Expression
        (a+b)
        (a+b
        (a+b}
        [a+b]
        [a+b)
        (1+2{f)
    '''

    while True:
        print("Enter an expression with parenthese (q to quit): ", end=' ')
        expression = input()
        if expression == 'q':
            break
        if is_valid(expression):
            print("Valid Expression")
        else:
            print("Invalid Expression")

