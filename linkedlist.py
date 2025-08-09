#LINKEDLIST:-
'''
* linked list is basically chains of nodes where each node contains information such as data and a pointer to the next
node in thr chain.
*In linkedlist ther is a node is present which contains data like string ,list etc and next pointer which indicates the
next node

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c

head = a
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

#LINKED LIST OPRERATION:- TRAVERSE, INSERT AND DELETE

# Traverse linked list

def printlinkedlist(head):
    curr = head

    while curr!=None:
        print(curr.data,end=' ')
        curr = curr.next

# printlinkedlist(head)

# Insertion at the begining

newNode =Node(4)
newNode.next = head
head = newNode
# printlinkedlist(head)

# insertion at the end

newNode = Node(1)

curr = head
while curr.next!=None:
    curr=curr.next

curr.next = newNode
# printlinkedlist(head)

#insertion at the kth index

k=2
newNode = Node(6)

curr = head
for i in range(k-1):
    curr = curr.next

newNode.next = curr.next
curr.next = newNode

# printlinkedlist(head)


# delete the first node

head = head.next
# printlinkedlist(head)

# delete last node

curr = head
while curr.next.next!=None:
    curr = curr.next

curr.next = None
# printlinkedlist(head)

# Delete the kth node

k=2

curr = head
for i in range(k-1):
    curr = curr.next

curr.next = curr.next.next
printlinkedlist(head)

#TYPES OF LINKED LIST:-- i).Singly linked list, ii).Doubly linked list, iii).Circular linked list

'''
*DLL-In Doubly linked list each data stores
         1].The data
         2].A link to the next node
         3].A link to the previous node

*It's like a two-way train:
       you can go forward and backward from any node
*Real life example.
                   i).You can go the next song
                   ii).Or you can go back to 
                   iii). 
'''
class DoublyNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.prev = a
b.next = c

head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)








































































































































































































