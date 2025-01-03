
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def visualize(self,head):
        
        while head:
            print(f"data is : {head.data}")
            head = head.next

        


ll = LinkedList()

arr = [2,3,4,5,6]

for val in arr:
    ll.add(val)


def search(head,key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False



value_bool = search(ll.head,10)
print(f"value exists in the linked list : {value_bool}")