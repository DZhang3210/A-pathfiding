from main import *

def heapify(arr, n, i):
    parent = int(((i - 1) / 2))
    # For Max-Heap
    # If current node is greater than its parent
    # Swap both of them and call heapify again
    # for the parent
    if arr[i].F < arr[parent].F \
            or (arr[i].F == arr[parent].F and arr[i].H < arr[parent].H):
        arr[i], arr[parent] = arr[parent], arr[i]
        # Recursively heapify the parent node
        heapify(arr, n, parent)

# Function to delete the root from Heap
def deleteRoot(arr):
    global n
    # Get the last element
    lastElement = arr[n - 1]
    # Replace root with last element
    arr[0] = lastElement
    # Decrease size of heap by 1
    n = n - 1
    # heapify the root node
    heapify(arr, n, 0)
    return lastElement

# Function to insert a new node to the Heap

def insertNode(arr, key):
    global n
    # Increase the size of Heap by 1
    n += 1
    # Insert the element at end of Heap
    arr.append(key)
    # Heapify the new node following a
    # Bottom-up approach
    heapify(arr, n, n - 1)


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
        print(currentNode.coords, end = " -> ")
        vector.append(currentNode.coords)
        currentNode = currentNode.prev
    print("Total Jumps", l - 1, ":|: Total Path Nodes", l)
    printPath(vector)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def printPath(vector):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (x,y) in vector:
                print("@", end = " ")
            else:
                print(board[x][y], end = " ")
        print(" ")

# nodes = [Node(None, start)]

#C represent the current Node
nodes = []
c = Node(None, start)
checked = {start:Node(None, start)}

nodes.append(c)
n=1
#Always choose the minimum object
while len(nodes) > 0:
    if (c.coords == end):
        print("Done DUN DUN DUUUN", c.coords)
        reverseChain(c)
        break

    print("Checking surroundings for ", c.coords)
    for i in c.getSurroundingNodes():
        if not(i.coords in checked.keys()):
            print(i.coords, "not in checking list")
            checked[i.coords] = i
            insertNode(nodes, checked[i.coords])
        elif(checked[i.coords].checked == False):
            print(i.coords, " in checking list")
            #Now there are two of the same node in the object
            if checked[i.coords].reev(c):
                insertNode(nodes, checked[i.coords])
    #Check over any duplicate Nodes
    checked[c.coords].checked = True
    n = len(nodes)
    while(n != 0 and checked[c.coords].checked == True):
        print(n)
        print("Already checked territory", c.coords)
        c = deleteRoot(nodes)
        n-=1
    if(n == 0):
        print("Can't Find Ending")
