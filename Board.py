import copy
from msilib import sequence
import random


class Board:

    def __init__(self, sequence = None):
        self.ResetBoard()

        if sequence:
            self.sequence = sequence

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(sequence[0])
                    sequence = sequence[1:]
        else:
            self.sequence = None

    def ResetBoard(self):
        self.board = [[0 for i in range(9)] for i in range(9)]

    def BoardToSequence(self, board = None):
        if board:
            sequence = ''.join([str(i) for j in board for i in j])
            return sequence
        else:
            self.sequence = ''.join([str(i) for j in self.board for i in j])
            return self.sequence
    
    def FindEmpty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def SquareIsValid(self, num, pos):

        # Check row for same number
        for col in range(len(self.board[0])):
            # Check if element in row has the same value, excluding itself
            if self.board[pos[0]][col] == num and pos[1] != col:
                return False

        # Check column for same number
        for row in range(len(self.board)):
            # Check if element in column has the same value, excluding itself
            if self.board[row][pos[1]] == num and pos[0] != row:
                return False

        # Check box for same number

        # Create box dimensions
        boxX = pos[1] // 3
        boxY = pos[0] // 3

        # Find box borders and iterate through box elements
        for i in range(boxY * 3, boxY * 3 + 3):
            for j in range(boxX * 3, boxX * 3 + 3):
                # Check if element in box has the same value, excluding itself
                if self.board[i][j] == num and pos != (i,j):
                    return False

        # Passes the tests, return true
        return True

    def PrintBoard(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
        
    def Solve(self):
        empty = self.FindEmpty()
        # Check if board is completed, and if so return
        if not empty:
            return True
        else:
            # Define row and column of empty cell
            row, col = empty
        
        for num in range(1, 10):
            if self.SquareIsValid(num, (row, col)):
                self.board[row][col] = num

                if self.Solve():
                    return True
                
                self.board[row][col] = 0

    def GenerateSolution(self, board):
        number_list = [1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row=i//9
            col=i%9
            #find next empty cell
            if board[row][col]==0:
                random.shuffle(number_list)      
                for number in number_list:
                    pos = (row, col)
                    if self.SquareIsValid(board, number, pos):
                        self.board.board[row][col]=number
                        if not self.FindEmpty():
                            return True
                        else:
                            if self.GenerateSolution(board):
                                #if the grid is full
                                return True
                break
        board[row][col]=0  
        return False
    
    def RemoveNumbersFromBoard(self, difficulty):
        if difficulty == 0:
            _squares_to_remove = 36
        elif difficulty == 1:
            _squares_to_remove = 46
        elif difficulty == 2:
            _squares_to_remove = 52
        