#!/usr/bin/env python
# coding:utf-8

"""
File: sudoku.py
Programmer: Luis David Socarras

- Sudoku solver algorithm implementing backtracking search 
using the minimum remaining value heuristic.
- boards.txt that contains samples of unsolved Sudoku boards, 
and sudoku_boards_solved.txt with their corresponding solutions.
Each board is represented as a single line of text, starting 
from the top-left corner of the board, and listed left-to-right,
top-to- bottom.

Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
from collections import defaultdict
from copy import copy
import time

ROW = "ABCDEFGHI"
COL = "123456789"
domain = defaultdict(set)


# creates a dictionary of sets with the domain
def get_domain(board):
    # Creating an empty dictionary
    global domain
    # domain = defaultdict(set)
    myDict = dict()
    newDomain = defaultdict(set)

    # Get all possibles values ( from 1 to 9)
    for i in ROW:
        for j in range(1, 10):
            domain[i].add(j)
    for i in COL:
        for j in range(1, 10):
            domain[i].add(j)
    # create domain for blocks
    for i in ROW:
        y0 = (ROW.index(i) // 3) * 3
        for j in COL:
            x0 = (COL.index(j) // 3) * 3
            # print(ROW[(y0)] + COL[(x0)])
            for k in range(1, 10):
                domain["BOX" + ROW[(y0)] + COL[(x0)]].add(k)

    # get all values from the table
    for i in ROW:
        for j in COL:
            if board[i + j] != 0:
                myDict.setdefault(i, []).append(board[i + j])
    for i in COL:
        for j in ROW:
            if board[j + i] != 0:
                myDict.setdefault(i, []).append(board[j + i])

    # add values from blocks
    for i in ROW:
        y0 = (ROW.index(i) // 3) * 3
        for j in COL:
            x0 = (COL.index(j) // 3) * 3

            if board[i + j] != 0:
                myDict.setdefault("BOX" +
                                  ROW[(y0)] + COL[(x0)], []).append(board[i + j])

    # updates domain with sudoku values
    for i in myDict:
        newDomain = domain[i].difference_update(myDict[i])


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

# find empty spot in the board and return it with the possible variables(domain)
def find_empty_and_domain(bo):
    row_ = None
    col_ = None
    x0_ = None
    y0_ = None
    min_intersection = {1,2,3,4,5,6,7,8,9}

    for row in ROW:
        for col in COL:
            # if spot is empty
            if bo[row + col] == 0:
                #get block index
                x0 = (ROW.index(row) // 3) * 3
                y0 = (COL.index(col) // 3) * 3
                # intersection to get only possible values
                intersection = domain[row].intersection(domain[col], domain["BOX" + ROW[x0] + COL[y0]])

                # if only one possible values, return value
                if len(intersection) == 1:
                    return (row, col, x0, y0, intersection)

                min_intersection = intersection
                row_ = row
                col_ = col
                x0_ = x0
                y0_ = y0
    return (row_, col_, x0_, y0_, min_intersection)

# Solve Sudoku board using backtracking search using the minimum remaining value heuristic.
def solve(bo):
    global domain

    # find empty spots
    find = find_empty_and_domain(bo)

    # if return None, board solved
    if find.__contains__(None):
        return True
    else:
        row, col, x0, y0, intersection = find

    # Try only possibles values from the domain
    for i in intersection:

        # add value to board
        bo[row + col] = i

        # Forward checking -> remove impossibles values from domain for next move
        domain[row].remove(i)
        domain[col].remove(i)
        domain["BOX" + ROW[x0] + COL[y0]].remove(i)

        if solve(bo):
            return True
        # backtracking when dead end
        bo[row + col] = 0
        domain[row].add(i)
        domain[col].add(i)
        domain["BOX" + ROW[x0] + COL[y0]].add(i)

    return False


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    get_domain(board)
    solve(board)
    solved_board = copy(board)
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudoku_boards.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    start_total_time = time.time()

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = {ROW[r] + COL[c]: int(line[9 * r + c])
                 for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        # print_board(board)
        start_time = time.time()

        # Solve with backtracking
        solved_board = backtracking(board)

        # print total time for each sudoku
        #print("--- %s seconds ---" % (time.time() - start_time))

        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")
    print("--- %s seconds ---" % (time.time() - start_total_time))
