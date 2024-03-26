from typing import Any


class Node:
    def __init__(self,value):
        self.data = value
        self.ref = None


class SingleLL():
    def __init__(self) -> None:
        self.head = None
        
    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head # creating a variable so that first node of the linked list dont lose
            while n is not None:
                print("Printing LL",n.data) # printing the data of the address of the node
                n=n.ref # Here we are stroting the address of next node 
        print("Traversal Complete")
                
    def add_at_beginning(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref = self.head
            self.head=new_node
            
    def add_at_end(self,value):
        new_node=Node(value)
        link=self.head
        while link is not None:
            if link.ref == None:
                link.ref=new_node
                break
            else:
                link=link.ref
                   
        
            


LL=SingleLL()
LL.traverse()
print("___________")
LL.add_at_beginning(10)
LL.traverse()
print("___________")
LL.add_at_beginning(100)
LL.traverse()
print("___________")
LL.add_at_beginning(200)
LL.traverse()
print("___________")
LL.add_at_beginning(400)
LL.traverse()
print("___________")
LL.add_at_end(1000)
LL.traverse()
print("___________")
LL.add_at_end(2000)
LL.traverse()
print("___________")
#print(node1,node1.data,node1.ref)