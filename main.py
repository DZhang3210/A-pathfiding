import heapq
#from MinHeap import *
#10 represents sideways movement
#14 Represents diagonal movement
dist = [10, 14]

#representing all movement directions
dir = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

#0 Stands for open space
#1 Stands for Flag
#2 Stands for obstacle
# start, end = (1,2),(4,6)
# board = [
#     [0,0,0,0,2,0,0,2,0,0],
#     [0,2,1,0,0,2,2,0,0,0],
#     [0,2,2,2,2,2,2,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0]
# ]
# start, end = (0,0), (4,5)
# board = [
#     [1,0,0,0,0,0],
#     [0,2,0,0,0,0],
#     [2,2,2,2,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,1]
# ]
# start, end = (0,0), (2,2)
# board = [
#     [1,0,0],
#     [2,0,0],
#     [0,0,1]
# ]

#THIS IS WHERE ALL CONSTANTS FOR PROBLEM ARE STORED






#On initialization knows the final end point, calculates G value and H values
#automatically and if we want to reevaluate we must only change the parent
# and check to see if it exists
class Node:
    #Instantiates coords, prev, and calculates G,H,F
    def __init__ (self, prev, end, coords):
        self.checked = False
        self.prev = prev
        self.end = end
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

    #Return true if anything changes, else return false
    def reev(self, prev):
        # If we are reevaluating Node then that means that prev G path must've
        # been updated
        testScore = self.getValueStart(prev, self.coords[0], self.coords[1]) + prev.G
        if(testScore < self.G):
            #Update prev, testScore and total
            self.prev = prev
            self.G = testScore
            self.F = self.G + self.H
            return True
        return False
    #Evaluating all import values from start/end
    def getValueEnd(self, end):
        total = 0
        x, y = abs(end[0] - self.coords[0]), abs(end[1] - self.coords[1])
        #print(x,y, end[0], end[1])
        while(x != 0 or y != 0):
            #print(x, y)
            if(x != 0 and y != 0):
                total += dist[1]
                x -= 1
                y -= 1
            else:
                total += dist[0]
                if(x != 0):
                    x-=1
                else:
                    y-=1
        return total

    def getValueStart(self, prev, x, y):
        if(prev == None):
            return 0
        return 14 if prev.coords[0] != x and prev.coords[1] != y else 10

    #Returns all surrounding Nodes to be returned to minHeap
    def getSurroundingNodes(self, board):
        currentX, currentY = self.coords[0], self.coords[1]
        returns = []
        for i in dir:
            #print("In direction")
            currentX += i[0]
            currentY += i[1]
            if(currentX >= 0 and currentX < len(board)
                and currentY >= 0 and currentY < len(board[0])
                and board[currentX][currentY] != 2):
                    returns.append(Node(self, self.end, (currentX, currentY)))
            currentX, currentY = self.coords[0], self.coords[1]
        return returns

    def printNode(self):
        print("==========")
        if(self.prev != None):
            print("Parents:",self.prev.coords)
        print(self.coords)
        print("G: ", self.G)
        print("H: ", self.H)
        print("F: ",self.F)
