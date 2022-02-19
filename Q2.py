"""
2. Tesla organizes their distribution system as a non-binary tree. The root of such tree is the source distributor, and every node in the tree represents another Tesla distributor that receives cars from the parent node and sends them to its children’s nodes. The leaves of the tree are the final dealers that sell cars to customers. Further, every node holds an integer representing the cost associated of shipping a car to it.
Tesla would like to compute the minimum cost in its distribution tree. Given a rootNode, write a program getMinimumCost that computes the minimum route’s cost in the tree. For example, given the root node of the tree above, your program should return 7 since it is the minimal route (we have two minimal cost paths: 0→6→1, 0→3→2→1→1).

"""

# A node
from collections import deque

queue = [] # hold last nodes


class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

    def add_child(self, cost):
        child = Node(cost)
        child.parent = self
        self.children.append(child)

# Recursive function that travels the tree and finds the leaf nodes
def inorder(root):
    if root is None:
        print("Error")
        return
    if len(root.children) == 0:
        # add leaf to the list
        queue.append(root)
    # travels through the nodes
    for i in root.children:
        inorder(i)



def getMinimumCost(root):
    path = 0
    heights = []  # store heights
    # gets the leaves
    inorder(root)

    #goes from leaf to parents untils gets to the root
    for i in queue:
        current = i
        while current.parent is not None:
            path = path + current.cost
            current = current.parent
        if current.parent is None:
            path = path + current.cost
        heights.append(path)
        path = 0
    return min(heights)

if __name__ == '__main__':

# Example tree
    root = Node(1)
    root.add_child(5)
    root.add_child(3)
    root.add_child(6)
    root.children[0].add_child(4)

    root.children[1].add_child(2)
    root.children[1].add_child(0)
    root.children[2].add_child(1)
    root.children[2].add_child(5)

    root.children[1].children[0].add_child(1)
    root.children[1].children[1].add_child(10)

    root.children[1].children[0].children[0].add_child(1)

    print("The minimum cost is %s" % getMinimumCost(root))
