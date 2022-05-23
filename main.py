import heapq
from MinHeap import *
#10 represents sideways movement
#14 Represents diagonal movement
dist = [10, 14]
start, end = (0,0), (5,4)

class Node:
    def __init__ (self, prev, val, coords):
        self.prev = prev
        self.val = val
        self.coords = coords

        #Main way of prioritizing and calculating next node in heap
        #Calculate G w/ previous path taken
        self.G = Node.getValue(start) + prev.G
        self.H = Node.getValue(end)
        self.F = self.G+self.H

    #Reassigning variables in case of new calculation
    def reev(self, prev, val, G, F):
        self.prev = prev
        self.val = val
        #If we are reevaluating Node then that means that prev G path must've
        #been updated
        self.G = G
        self.F = self.G + self.H

    #Evaluating all import values from start/end
    def getValue(self, point, parent = None):
        total = 0
        x, y = self.coords[0], self.coords[1]
        while(point[0] != x or point[1] != y):
            if(point[0] != x and point[1] != y):
                total += dist[1]
            else:
                total+= dist[0]
        return total


#representing all movement directions
dir = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
#must calculate distance away from starting and away from ending

#0 Stands for open space
#1 Stands for Flag
#2 Stands for obstacle
list = [
    [1,0,0,0,0,0]
    [0,2,0,0,0,0]
    [2,2,2,2,0,0]
    [0,0,0,0,0,0]
    [0,0,0,0,0,1]
]

