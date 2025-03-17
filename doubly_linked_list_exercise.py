class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def print_forward(self):
        if self.head is None:
            return print('Empty linked list!')

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def print_backward(self):
        if self.head is None:
            return print('Empty linked list!')

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.prev
        print(llstr)




li = LinkedList()
li.insert_at_end('23')
li.insert_at_end('34')
li.insert_at_end('65')
li.print_forward()
li.print_backward()


