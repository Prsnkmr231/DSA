

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self,head,value):
        current = self.head
        while current:
            if current.data==value:
                current.data = current.next.data
                current.next = current.next.next
                break
            else:
                current = current.next
        



        
    



    def visualize(self,head):
        current = head
        while current:
            print(f"data is : {current.data}")
            current = current.next
        


arr = [1,2,3,4]
ll = LinkedList()
for val in arr:
    ll.append(val)

ll.visualize(ll.head)

ll.delete(ll.head,3)

print(f"printing the linked list after deleting the node")
ll.visualize(ll.head)
            

