
class Node:
    def __init__(self,value):
        self.data = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def visulaize(self,head):
        current = head
        while current:
            print(current.data,end="<--->")
            current = current.next
        print("None")


arr = [2,3,4,5,6]
ll = LinkedList()
for value in arr:
    ll.insert(value)

ll.visulaize(ll.head)


        
        