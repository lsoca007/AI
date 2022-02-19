"""
3. Given the root of a binary tree, using DFS, return the tree’s nodes as if you were doing the following: 
3.1 get all the leaf nodes
3.2 remove all leaf nodes
3.3 repeat previous two steps until the tree is empty.
"""

leaves = []  # store the leaf nodes
COUNT = [10]  # count for printing the tree


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"


def printTreeUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    printTreeUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)

    # Process left child
    printTreeUtil(root.left, space)


# Wrapper over print2DUtil()
def printTree(root):
    # space=[0]
    # Pass initial space count as 0
    printTreeUtil(root, 0)


# Remove the leaf nodes form the tree and store it into a list
def remove_leaves(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        leaves.append(root.value)  # get the leaf nodes into a list
        return None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root


# Use DFS to get the height of the tree
def maxDepth(node):
    if node is None:
        return -1

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1


# remove all leaf nodes until the tree is empty.
def delete_in_cascade(root):
    while True:
        remove_leaves(root)
        print(leaves)
        leaves.clear()
        printTree(root)
        if maxDepth(root) == 0:
            leaves.append(root.value)
            print(leaves)
            leaves.clear()
            break


# Pre-Order DFS
def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)


if __name__ == '__main__':
    # Example 1
    print("-------Example 1---------")
    root = Node('1', Node('2', Node('4'), Node('5')), Node('3'))
    printTree(root)
    delete_in_cascade(root)
    # Example 2
    print("-------Example 2--------")
    mytree = Node('1', Node('2', Node('4'), Node('5')), Node('3', Node('6'), Node('7')))
    printTree(mytree)
    delete_in_cascade(mytree)
