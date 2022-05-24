from main import *

#Use dictionary to update and check if it exists in real time
class MinNode:
    def __init__ (self, Node, left = None, right= None):
        #Main way of traversing heap
        self.left = left
        self.right = right
        #Value in heap
        self.Node = Node #remember that we can also check Node.f

class MinHeap:
    def __init__ (self):
        self.head = None

    # def insert(self, Node):
    #     if(self.head == None):
    #         self.head = MinNode(Node)
    #     else:
    #         currentCheck = self.head
    #         if(Node.val )

#set1 = {(0,0),MinNode(Node(None, (0,0)))}