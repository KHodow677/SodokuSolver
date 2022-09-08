import copy
import random


class Board:
    def __init__(self, code=None):
        self._ResetBoard()

        if code:
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]
        else:
            self.code = None

    def _ResetBoard(self):
        self.board = [[0 for i in range(9)] for i in range(9)]

myBoard = Board()
print(myBoard.board)