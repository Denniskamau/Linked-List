""" 
Finding the middle element in a linked list.
"""

#Create a linked list with connecting nodes
class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = next

# setup some nodes and connect them to each other
# the linked list looks like:
# (head) n5 -> n4 -> n3 -> n2 -> n1 -> None
n1 = Node("Hello", None)  
n2 = Node("21", n1)
n3 = Node("Green", n2) 
n4 = Node("Blue", n3)
n5 = Node("Daniel", n4)

"""
Assing a node to the head which functions as the
Entry point to the linked list
"""
head = n5
fastPointer = head
slowPointer = head

# loop through the linked list
# when fastPointer reaches the end of the list
# then slowPointer will be at the middle node
while fastPointer.next != None and fastPointer.next.next != None:
  fastPointer = fastPointer.next.next
  slowPointer = slowPointer.next
  
# slowPointer is now at the middle node in the linked listou
print (slowPointer.data)            