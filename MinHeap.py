from main import *

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