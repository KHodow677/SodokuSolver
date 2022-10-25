import copy
from msilib import sequence
import random
import pygame
class Board:
    # Constructor of Board class (input sequence string optional)
    def __init__(self, screen, sequence = None):
        self.ResetBoard()
        self.screen = screen
        if sequence:
            self.sequence = sequence

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(sequence[0])
                    sequence = sequence[1:]
        else:
            self.sequence = None

    # Method that clears the board and resets it to all zeros
    def ResetBoard(self):
        self.board = [[0 for i in range(9)] for i in range(9)]

    # Method that returns a string representation of the board state, aka sequence
    def BoardToSequence(self, board = None):
        if board:
            sequence = ''.join([str(i) for j in board for i in j])
            return sequence
        else:
            self.sequence = ''.join([str(i) for j in self.board for i in j])
            return self.sequence
    
    # Method that returns the next empty square in the board sequence
    def FindEmpty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    # Method that checks of a number in a square is valid depending on its row, column, and box
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

    # Method that prints an ASCII representation of the board to console (obsolete)
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

    # Method that uses pygame to draw the GUI representation of th board
    def Draw(self):
        # Load test fonts for future use
        font1 = pygame.font.SysFont("comicsans", 40)
        dif = 500 / 9
        # Draw the lines
        for i in range (9):
            for j in range (9):
                if self.board[i][j]!= 0:
    
                    # Fill blue color in already numbered grid
                    pygame.draw.rect(self.screen, (204, 85, 0), (i * dif, j * dif, dif + 1, dif + 1))
    
                    # Fill grid with default numbers specified
                    text1 = font1.render(str(self.board[i][j]), 1, (0, 0, 0))
                    self.screen.blit(text1, (i * dif + 15, j * dif))
        # Draw lines horizontally and vertically to form grid          
        for i in range(10):
            if i % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick) 
    
    # Method that uses recursive backtracking to solve the board and complete it
    def Solve(self):
        self.Draw()
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

    # Method that generates a full board solution with no missing numbers
    def GenerateSolution(self):
        number_list = [1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row=i//9
            col=i%9
            #find next empty cell
            if self.board[row][col]==0:
                random.shuffle(number_list)      
                for number in number_list:
                    pos = (row, col)
                    if self.SquareIsValid(number, pos):
                        self.board[row][col]=number
                        if not self.FindEmpty():
                            return True
                        else:
                            if self.GenerateSolution():
                                #if the grid is full
                                return True
                break
        self.board[row][col]=0  
        return False
    
    # Method that removes numbers from the board in quantities depending on difficulty
    # Removes numbers in an even spread
    def RemoveNumbersFromBoard(self, difficulty):
        if difficulty == 0:
            squares_to_remove = 36
        elif difficulty == 1:
            squares_to_remove = 46
        elif difficulty == 2:
            squares_to_remove = 52
        
        # Remove numbers from section 1
        counter = 0
        while counter < 4:
            rRow = random.randint(0, 2)
            rCol = random.randint(0, 2)
            if self.board[rRow][rCol] != 0:
                self.board[rRow][rCol] = 0
                counter += 1

        # Remove numbers from section 2
        counter = 0
        while counter < 4:
            rRow = random.randint(3, 5)
            rCol = random.randint(3, 5)
            if self.board[rRow][rCol] != 0:
                self.board[rRow][rCol] = 0
                counter += 1

        # Remove numbers from section 3
        counter = 0
        while counter < 4:
            rRow = random.randint(6, 8)
            rCol = random.randint(6, 8)
            if self.board[rRow][rCol] != 0:
                self.board[rRow][rCol] = 0
                counter += 1

        # Remove remaining numbers
        squares_to_remove -= 12
        counter = 0
        while counter < squares_to_remove:
            rRow = random.randint(0, 8)
            rCol = random.randint(0, 8)

            if self.board[rRow][rCol] != 0:
                n = self.board[rRow][rCol]
                self.board[rRow][rCol] = 0
                counter += 1