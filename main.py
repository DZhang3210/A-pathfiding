import heapq
#from MinHeap import *
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
    [1,0,0,0,0,0],
    [0,2,0,0,0,0],
    [2,2,2,2,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1]
]

#On initialization knows the final end point, calculates G value and H values
#automatically and if we want to reevaluate we must only change the parent
# and check to see if it exists
class Node:
    #Instantiates coords, prev, and calculates G,H,F
    def __init__ (self, prev, coords):
        self.checked = False
        self.prev = prev
        self.coords = coords

        #Main way of prioritizing and calculating next node in heap
        #Calculate G w/ previous path taken
        self.G = self.getValueStart(prev, self.coords[0], self.coords[1])
        if(prev != None):
            self.G += prev.G
        self.H = self.getValueEnd(end)
        self.F = self.G + self.H

    #Automatically Reassigning new F based on new prev if new path is
    #more optimized
    def reev(self, prev):
        # If we are reevaluating Node then that means that prev G path must've
        # been updated
        testScore = self.getValueStart(prev, self.coords[0], self.coords[1]) + prev.G
        if(testScore < self.G):
            #Update prev, testScore and total
            self.prev = prev
            self.G = testScore
            self.F = self.G + self.H

    #Evaluating all import values from start/end
    def getValueEnd(self, point):
        total = 0
        x, y = abs (point[0] - self.coords[0]), abs(point[1] - self.coords[1])
        while(x != 0 or y != 0):
            if(x != 0 and y != 0):
                total += dist[1]
                x -= 1
                y -= 1
            else:
                total += dist[0]
                if(point[0] != x):
                    x-=1
                else:
                    y+=1
        return total

    def getValueStart(self, prev, x, y):
        if(prev == None):
            return 0
        return 14 if prev.coords[0] != x and prev.coords[1] != y else 10

    #Returns all surrounding Nodes to be returned to minHeap
    def getSurroundingNodes(self):
        currentX, currentY = self.coords[0], self.coords[1]
        nodes = []
        for i in dir:
            #print("In direction")
            currentX += i[0]
            currentY += i[1]
            if(currentX >= 0 and currentX < len(board[0])
                and currentY >= 0 and currentY < len(board)
                and board[currentX][currentY] != 2):
                    nodes.append(Node(self, (currentX, currentY)))
            currentX, currentY = self.coords[0], self.coords[1]

        return nodes

    def printNode(self):
        print("==========")
        if(self.prev != None):
            print("Parents:",self.prev.coords)
        print(self.coords)
        print("G: ", self.G)
        print("H: ", self.H)
        print("F: ",self.F)

#Unable to test reev so far
# c = Node(None, (1,0))
# c.printNode()
# for i in c.getSurroundingNodes():
#     i.printNode()

