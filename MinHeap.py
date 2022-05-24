from main import *

def heapify(arr, n, i):
    parent = int(((i - 1) / 2))
    # For Max-Heap
    # If current node is greater than its parent
    # Swap both of them and call heapify again
    # for the parent
    if arr[i].F < arr[parent].F:
        arr[i], arr[parent] = arr[parent], arr[i]
        # Recursively heapify the parent node
        heapify(arr, n, parent)

# Function to delete the root from Heap
# def deleteRoot(arr):
#     global n
#     # Get the last element
#     lastElement = arr[n - 1]
#     # Replace root with last element
#     arr[0] = lastElement
#     # Decrease size of heap by 1
#     n = n - 1
#     # heapify the root node
#     heapify(arr, n, 0)


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

# nodes = [Node(None, start)]
# checked = {(0,0):Node(None, start)}
nodes = []
c = Node(None, (0,0))
nodes.append(c)
n=1
for i in c.getSurroundingNodes():
    insertNode(nodes, i)
printArray(nodes, n)

