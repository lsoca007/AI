"""
1. Given a matrix of 0s and 1s that represent the state space of a search problem, we have a starting row and column given by a tuple (starting_row, starting_column), and a target row and column (target_row, target_column). Implement an algorithm that outputs the length of the shortest path from (starting_row, starting_column) to (target_row, target_column) where the path contains only 1 values along the way.
Note that each location in the path (including the start and target), must be a 1.
Each subsequent location in the path must be a 4-directionally adjacent to the previous (north, south, east, west).
If the task is not possible, the algorithm should return -1.
"""

# Node class for the current location
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# find the shortest distance from starting location to the target using BFS on a matrix
def shortest_path_length (startV, targetV, matrix):

    # get current position
    currentV = Node(startV[0], startV[1])

    #list with children
    nextToVisit = []
    #stored shortest distance
    minDistance =0

    #get the visited matrix initialized to all false
    visited = [[False for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]

    # BFS
    nextToVisit.append(currentV)
    visited[currentV.row][currentV.col] = True
    while len(nextToVisit) != 0:
        currentV = nextToVisit.pop() # remove from next to visit

        if currentV.row == targetV[0] and currentV.col == targetV[1]:
            return minDistance


        #going UP
        if isValid (currentV.row -1, currentV.col,matrix,visited):
            nextToVisit.append(Node(currentV.row -1 , currentV.col))
            minDistance =minDistance + 1
            visited[currentV.row -1][currentV.col] = True

        #DOWN
        if isValid (currentV.row +1, currentV.col,matrix,visited):
            nextToVisit.append(Node(currentV.row +1 , currentV.col))
            minDistance =minDistance +1
            visited[currentV.row +1][currentV.col] = True

        #LEFT
        if isValid (currentV.row, currentV.col-1,matrix,visited):
            nextToVisit.append(Node(currentV.row , currentV.col-1))
            minDistance =minDistance +1
            visited[currentV.row][currentV.col-1] = True

        # RIGHT
        if isValid(currentV.row, currentV.col + 1, matrix,visited):
            nextToVisit.append(Node(currentV.row, currentV.col + 1))
            minDistance = minDistance +1
            visited[currentV.row][currentV.col + 1] = True
    return -1

#check if next position is valid
def isValid(row, column, matrix, visited):
    if ((row >= 0 and column >= 0) and
        (row < len(matrix) and column < len(matrix[0])) and
            (matrix[row][column] != 0) and (visited[row][column] == False)):
        return True
    return False



if __name__ == '__main__':

   #Example 1
    startV = (0,0)
    targetV = (2,0)
    matrix = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]


    print(shortest_path_length(startV, targetV, matrix))

   #Example 2

    startV = (0, 0)
    targetV = (2, 0)
    matrix = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]

    print(shortest_path_length(startV, targetV, matrix))