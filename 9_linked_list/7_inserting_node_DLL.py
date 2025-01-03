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
arr = [6,5,5,6,3,5,8]
ll = LinkedList()
for value in arr:
    ll.insert(value)

ll.visulaize(ll.head)


def addNode(head, p, x):
        new_node = Node(x)
        current = head
        count = 0
        while current :
            if (count+1)>p:
                break
            current = current.next
            count+=1
        # print(count)
        # print(type(current))
        if (current and ((count+1)>p)):
            temp = None
            if current.next is None:
                temp = None
            else:
                temp = current.next
            current.next = new_node
            new_node.next = temp
            new_node.prev = current
            
        
        return head
            
        
        

addNode(ll.head,6,7)

ll.visulaize(ll.head)