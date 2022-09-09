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