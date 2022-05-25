from main import *
import pygame
from pygame.locals import *
from MinHeap import *

pygame.init()
display_width = 603
display_height = 700
dif = display_width//100
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pathfinding")
game_display.fill((255,255,255))
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 16)



def heapifyDel(arr, n, i):
    smallest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if (l < n and (arr[l].F < arr[smallest].F or (arr[l].F == arr[smallest].F and arr[l].H < arr[smallest].H))):
        smallest = l
    # If right child is larger than largest so far
    if (r < n and (arr[r].F < arr[smallest].F or (arr[r].F == arr[smallest].F and arr[r].H < arr[smallest].H))):
        smallest = r
    # If largest is not root
    if (smallest != i):
        arr[i], arr[smallest] = arr[smallest], arr[i]
        # Recursively heapify the affected sub-tree
        heapifyDel(arr, n, smallest)

def heapifyIns(arr, n, i):
    parent = int(((i - 1) / 2))
    if(parent >= 0):
        if arr[i].F < arr[parent].F or (arr[i].F == arr[parent].F and arr[i].H < arr[parent].H):
            arr[i], arr[parent] = arr[parent], arr[i]
            # Recursively heapify the parent node
            heapifyIns(arr, n, parent)

# Function to delete the root from Heap
def deleteRoot(arr):
    global n
    min = arr[0]
    if(n > 1):
        arr[0] = arr[n-1]
    n -= 1
    heapifyDel(arr, n, 0)
    return min

# Function to insert a new node to the Heap

def insertNode(arr, key):
    global n
    if(len(arr) <= n):
        arr.append(key)
    else:
        arr[n] = key
    n += 1
    heapifyIns(arr, n, n - 1)


# A utility function to print array of size n
def printArray(arr, n):
    for i in range(n):
        arr[i].printNode()

def reverseChain(node):
    currentNode = node
    l = 0
    vector = []
    while(currentNode != None):
        l+=1
        print(currentNode.coords, end = " <- ")
        vector.append(currentNode.coords)
        currentNode = currentNode.prev
    print("Total Jumps", l - 1, ":|: Total Path Nodes", l)
    printPath(vector)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def printPath(vector):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (x,y) in vector:
                if((x,y) == start or (x,y) == end):
                    print("$", end = " ")
                else:
                    print("@", end = " ")
            else:
                print(board[x][y], end = " ")
        print(" ")

def printHeap(lst):
    for i in range(n):
        print("(", i.coords[1],",",i.coords[0],")", end = " ")
        print(" : ", lst[i].F,"other", lst[i].H)


# nodes = [Node(None, start)]

#C represent the current Node
def pathFinding():
    #Always choose the minimum object
    while len(nodes) > 0:
        c = deleteRoot(nodes)
        while (len(nodes) > 0 and checked[c.coords].checked == True):
            c = deleteRoot(nodes)
        checked[c.coords].checked = True

        if (c.coords == end):
            print("Done DUN DUN DUUUN")
            reverseChain(c)
            break

        #print("Checking (", c.coords[1],",",c.coords[0],")")
        for i in c.getSurroundingNodes():
            if not(i.coords in checked.keys()):
                #print("Inserting element ", i.coords, "through New")
                checked[i.coords] = i
                insertNode(nodes, checked[i.coords])
            elif(checked[i.coords].checked == False):
                #Now there are two of the same node in the object
                #print("Inserting element ", i.coords, "through Extra")
                if checked[i.coords].reev(c):
                    insertNode(nodes, checked[i.coords])

        #Check over any duplicate Nodes
    if(n == 0):
        print("Can't Find Ending")

nodes = []
checked = {start:Node(None, start)}
nodes = [Node(None, start)]
n = 1
#pathFinding()
tile_size = 20
hBuffer, vBuffer, spacing = display_width//(8*tile_size),display_height//(5*tile_size),1
xBegin, xEnd = hBuffer, (display_width//tile_size) - hBuffer
yBegin, yEnd = vBuffer, (display_height//tile_size)
for x in range(xBegin, xEnd):
    for y in range(yBegin, yEnd):
        pygame.draw.rect(game_display, (0, 155,155) , [x*tile_size, y*tile_size, tile_size-spacing, tile_size-spacing], 0)
boldness = 3;
pygame.draw.line(game_display, (0, 0, 0), (xBegin*tile_size,yBegin*tile_size), (xEnd*tile_size, yBegin*tile_size), boldness)
pygame.draw.line(game_display, (0, 0, 0), (xBegin*tile_size, yBegin*tile_size), (xBegin*tile_size, yEnd*tile_size), boldness)
pygame.draw.line(game_display, (0, 0, 0), (xEnd*tile_size, yBegin*tile_size), (xEnd*tile_size, yEnd*tile_size), boldness)
#pygame.draw.line(game_display, (0, 0, 0), (2*display_width//3, 0), (2*display_width//3, display_width), boldness)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        # Check if you need to quit program
        if (event.type == QUIT or (
                event.type == KEYDOWN and (
                event.key == K_ESCAPE or
                event.key == K_q
        ))):
            pygame.quit()
            quit()