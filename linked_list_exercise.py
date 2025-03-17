class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
             itr = itr.next

        itr.next = Node(data, None)


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



    def insert_after_value(self, value, data):
        if self.head is None:
            return

        if self.head == value:
            self.head.next = Node(data, self.head.next)



        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            raise Exception("Empty linkedlist.")

        if self.head == value:
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break

            itr = itr.next


    def print(self):
        if self.head is None:
            return print("This is an empty linked list.")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)


li = LinkedList()
li.insert_values(['mango', 'apple', 'jackfruit'])
li.print()

li.insert_after_value('apple', 'litchi')
li.print()

li.remove_by_value('apple')

li.print()




