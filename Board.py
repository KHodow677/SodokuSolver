import copy
from msilib import sequence
import random


class Board:
    def __init__(self, sequence = None):
        self._ResetBoard()

        if sequence:
            self.sequence = sequence

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(sequence[0])
                    sequence = sequence[1:]
        else:
            self.sequence = None

    def _ResetBoard(self):
        self.board = [[0 for i in range(9)] for i in range(9)]

    def boardToSequence(self, input_board = None):
        if input_board:
            sequence = ''.join([str(i) for j in input_board for i in j])
            return sequence
        else:
            self.sequence = ''.join([str(i) for j in self.board for i in j])
            return self.sequence
