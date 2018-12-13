import numpy as np
import tensorflow as tf


class Twenty48():
"""Simple 2048 game played on a matrix."""

    def __init__(self, dimensions=4):
        """Create game board matrix and create 2 random numbers on the board.

        dimensions -- length and width of game board (4 by default)
        """
        self.size = dimensions

        #create empty board filled with zeroes of size provided
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.add_to_board(2)

    def add_to_board(self, num):
        """Add 2 or 4 to game board. 90% chance of 2, 10% chance of 4.

        num -- number of random numbers to place on board
        """
        for i in range(num):
            #Keep repeating until coordinate is selected that is empty.
            while collision:
                x_coord = np.random.randint(self.size)
                y_coord = np.random.randint(self.size)
                value = 4 if np.random.rand() > 0.9 else 2  # Select value of tile
                # Add value to board at coordinate if the coordinate is empty
                if self.board[y_coord][x_coord] == 0:
                    self.board[x_coord][y_coord] = value
                    break
