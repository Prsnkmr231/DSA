class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

def create_LL(arr):
    ll = Linkedlist()
    for index in range(len(arr)):
        ll.append(arr[index])

    return ll

arr = [1,2,3,4]

value = create_LL(arr)

value.display()

            