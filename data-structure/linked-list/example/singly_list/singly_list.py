from base import SingleLinkedList, Node


class Practice(SingleLinkedList):
    # add element at the beginning
    def push(self, value):
        '''
            This function is used to add element at the beginning
            params:
                value: any type
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    # add element at the end
    def append(self, value):
        '''
            This function is used to add element at the end of list
            params:
                value: any type
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        return



    def insert_after_value(self, value, x):
        '''
            This function is used to add element after given value
            params:
                value: any type
                x : any type
        '''
        if self.head is None:
            raise Exception("List has no items")

        new_node = Node(value)
        current = self.head
        while current:
            if current.data == x:
                break
            current = current.next
        
        if current is None:
            raise Exception("{} not exists in list".format(x))

        new_node.next = current.next
        current.next = new_node

            
    def insert_before_value(self, value, x):
        '''
            This function is used to add element before given value
            params:
                value: any type
                x : any type
        '''
        if self.head is None:
            raise Exception("List has no items")

        new_node = Node(value)

        # if first node has matched condition
        if self.head.data == x:
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.head
        while prev:
            if prev.next.data == x:
                break
            prev = prev.next
        
        if prev is None:
            raise Exception("{} not exists in list".format(x))

        new_node.next = prev.next
        prev.next = new_node
        



if __name__ == "__main__":
    try:
        obj = Practice()
        obj.push(20)
        obj.push(30)
        obj.append(5)
        obj.print_list()
        print('-'*50)
        # obj.insert_after_value(10, 5)
        obj.insert_before_value(1, 30)
        obj.print_list()
    except Exception as e:
        print(e)

