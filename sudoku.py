import sys
import time 
import numpy as np
from itertools import accumulate

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"
sys.setrecursionlimit(10**6)

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

   


def backtracking(board):
    number= count(board)
    while number>1:
        for i in range(0,9):
            for j in range(0,9):
                if board.get(ROW[i]+COL[j]) == 0: # find empty space / MVH
                    for dig in range(1,10):
                        if working(dig, board, i, j): # forward checking 
                            board[ROW[i]+COL[j]] = dig                   
                            number=number-1                                                                       
    solved_board = board
    return solved_board
                                                                                           
    

def working(digit, board, row, col):
    
       #check 3*3 squars 
        s_row = (row//3)*3
        s_col = (col//3)*3     
        for i in range(0,3):
            for j in range(0,3):
                if board[ROW[s_row +i]+COL[s_col+j]] == digit:
                    return False      
       # check column 
        for i in range(0,9):
            for j in range(col-1,col):
                if board[ROW[i]+COL[j]] == digit and (i,j) != (row, col):
                    return False 
         #check row 
        for i in range(row-1,row):
            for j in range(0,9):
                if board[ROW[i]+COL[j]] == digit and (i,j) != (row, col):
                    return False 
        #check 3*3 squars again  
        s_row = (row//3)*3
        s_col = (col//3)*3     
        for i in range(0,3):
            for j in range(0,3):
                if board[ROW[s_row +i]+COL[s_col+j]] == digit:
                    return False 
              
        return True
    


def empty(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[ROW[i]+COL[j]] == 0:
                return True

    return False 

def count(board):
    x=0     
    for i in range(0,9):
        for j in range(0,9):
            if board[ROW[i]+COL[j]] == 0:
                x=x+1 
     
    return x 

if __name__ == '__main__':

    if len(sys.argv) > 1:

        #  Read individual board from command line arg.
        sudoku = sys.argv[1]

        if len(sudoku) != 81:
            print("Error reading the sudoku string %s" % sys.argv[1])
        else:
            board = { ROW[r] + COL[c]: int(sudoku[9*r+c])
                      for r in range(9) for c in range(9)}
            print(count(board))
           
            print_board(board)
           
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()

            print_board(solved_board)

            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

    else:

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                    for r in range(9) for c in range(9)}
          
            
            # Print starting board.
            
            print_board(board)
            
            # Solve with backtracking
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            

            # Print solved board. 
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")
