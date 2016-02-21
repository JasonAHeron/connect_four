import numpy as np


class GameBoard(object):

    def __init__(self, columns=7, rows=5):
        self.columns = columns
        self.rows = rows
        self.board_state = np.matrix([['*'] * columns for row in range(rows)])
        self.winner = None

    def __str__(self):
        return '\n'.join('   '.join(row) for row in self.board_state.tolist())

    def insert_piece(self, column, piece):
        #make sure we're trying a valid move
        try:
            if int(column) not in range(self.columns):
                return False
        except ValueError:
            return False
        else:
            column = int(column)

        #check from the bottom up and replace first '*' we see
        for row in self.board_state[::-1]:
            if row[0,column] == '*':
                row[0,column] = piece
                #if we can insert the piece check if that player has won
                self.check_win(piece)
                return True
        # if the insert fails allow the caller to handle it
        return False

    def check_win(self, piece):
        if (
          self.check_win_vertical(piece)
          or
          self.check_win_horizonal(piece)
          or
          self.check_win_diagonal(piece)
        ):
            self.winner = piece

    def check_win_vertical(self, piece):
        #transpose matrix to check columns as if they were rows
        for column in self.board_state.T.tolist():
            if piece * 4 in ''.join(column):
                return True
        return False

    def check_win_horizonal(self, piece):
        for row in self.board_state.tolist():
            if piece * 4 in ''.join(row):
                return True
        return False

    def check_win_diagonal(self, piece):
        #http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        diagonals = [self.board_state[::-1,:].diagonal(i) for i in range(-self.board_state.shape[0]+1,self.board_state.shape[1])]
        diagonals.extend(self.board_state.diagonal(i) for i in range(self.board_state.shape[1]-1,-self.board_state.shape[0],-1))
        for diagonal in diagonals:
            if piece * 4 in ''.join(diagonal.tolist()[0]):
                return True
        return False
