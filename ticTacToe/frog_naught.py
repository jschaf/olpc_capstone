'''Frog TicTac - A simple tic tac toe game for the OLPC project.

'''

class Cell(object):
    '''A enum of possible tic-tac-toe square values.'''
    CROSS = 1                  # an 'X'
    NAUGHT = 0                  # an 'O'
    EMPTY = -1


class InputError(Exception):
    '''Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    '''

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TicTacToe(object):
    '''A matrix of Cells to represent a tic-tac-toe board.

    Attributes:
    size -- the width and height of the tic-tac-toe board
    '''
    def __init__(self, size=3):
        self.size = size
        self.board = [[Cell.EMPTY for _ in range(self.size)] for _ in range(3)]

    def __str__(self):
        def cell_to_string(mark):
            '''Return a string representation of a Cell enum.'''
            if mark == Cell.NAUGHT:
                return 'O'
            elif mark == Cell.CROSS:
                return 'X'
            elif mark == Cell.EMPTY:
                return ' '

        build_row = lambda row: [cell_to_string(elem) for elem in row]
        row_strings = ['|'.join(build_row(row)) for row in self.board]
        return '\n-+-+-\n'.join(row_strings)

    def is_won_by(self, cell):
        '''Return true if the given cell has won, else return false.

        Keyword arguments:
        cell -- which Cell enum to check for a win
        '''
        all_match = lambda a, b, c: cell == a == b == c

        check_rows = any([all_match(*row) for row in self.board])
        check_cols = any([all_match(*col) for col in zip(*self.board)])

        check_right_diag = all_match(*[self.board[i][i]
                                       for i in range(self.size)])

        check_left_diag = all_match(*[self.board[self.size - 1 - i][i]
                                      for i in range(self.size)])

        return (check_rows or check_cols or check_right_diag
                or check_left_diag)

    def mark_cell(self, cell, row, col):
        '''Insert cell at (row,col) if it is empty.

        Keyword arguments:
        cell -- the Cell enum to insert
        row -- which row of the board to insert the cell
        col -- which col of the board to insert the cell
        '''
        if self.board[row][col] == Cell.EMPTY:
            self.board[row][col] = cell
        else:
            raise InputError(self.board == 1,
                             'Tried to mark a previously marked cell.')
