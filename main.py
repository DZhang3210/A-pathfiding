import heapq
from MinHeap import *
#10 represents sideways movement
#14 Represents diagonal movement
dist = [10, 14]
start, end = (0,0), (5,4)
#representing all movement directions
dir = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

#0 Stands for open space
#1 Stands for Flag
#2 Stands for obstacle
board = [
    [1,0,0,0,0,0]
    [0,2,0,0,0,0]
    [2,2,2,2,0,0]
    [0,0,0,0,0,0]
    [0,0,0,0,0,1]
]

class Node:
    def __init__ (self, prev, coords):
        self.prev = prev
        self.coords = coords

        #Main way of prioritizing and calculating next node in heap
        #Calculate G w/ previous path taken
        self.G = Node.getValue(start) + prev.G
        self.H = Node.getValue(end)
        self.F = self.G+self.H

    #Reassigning variables in case of new calculation
    def reev(self, prev, val, G):
        self.prev = prev
        self.val = val
        #If we are reevaluating Node then that means that prev G path must've
        #been updated
        self.G = G + prev.G
        self.F = self.G + self.H

    #Evaluating all import values from start/end
    def getValue(self, p, point, parent = None):
        total = 0
        x, y = p[0], p[1]
        while(point[0] != x or point[1] != y):
            if(point[0] != x and point[1] != y):
                total += dist[1]
            else:
                total += dist[0]
        return total

    #Returns all surrounding Nodes to be returned to minHeap
    def getSurroundingNodes(self):
        currentX, currentY = self.coords[0], self.coords[1]
        nodes = []
        for i in dir:
            currentX += i[0]
            currentY += i[1]
            if(currentX > 0 and currentX < len(board[0])
                and currentY > 0 and currentY < len(board)
                and board[currentX][currentY] != 1):
                    nodes.append(Node(self, (currentX, currentY)))

            currentX, currentY = self.coords[0], self.coords[1]




