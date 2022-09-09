import Board

class SodokuSolver:

    def __init__(self, sequence = None):
        self.board = Board.Board(sequence = sequence)

    def PrintBoard(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def FindEmpty(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def SquareIsValid(self, board, num, pos):

        # Check row for same number
        for col in range(len(board[0])):
            # Check if element in row has the same value, excluding itself
            if board[pos[0]][col] == num and pos[1] != col:
                return False

        # Check column for same number
        for row in range(len(board)):
            # Check if element in column has the same value, excluding itself
            if board[row][pos[1]] == num and pos[0] != row:
                return False

        # Check box for same number

        # Create box dimensions
        boxX = pos[1] // 3
        boxY = pos[0] // 3

        # Find box borders and iterate through box elements
        for i in range(boxY * 3, boxY * 3 + 3):
            for j in range(boxX * 3, boxX * 3 + 3):
                # Check if element in box has the same value, excluding itself
                if board[i][j] == num and pos != (i,j):
                    return False

        # Passes the tests, return true
        return True
        
    def Solve(self, board):
        empty = self.FindEmpty(board)
        # Check if board is completed, and if so return
        if not empty:
            return True
        else:
            # Define row and column of empty cell
            row, col = empty
        
        for num in range(1, 10):
            if self.SquareIsValid(board, num, (row, col)):
                board[row][col] = num

                if self.Solve(board):
                    return True
                
                board[row][col] = 0
        