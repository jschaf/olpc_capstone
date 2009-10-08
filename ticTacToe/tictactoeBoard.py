'''tictactoeBoard - A simple tic-tac-toe representation.

'''

class Cell(object):
    '''A enum of possible tic-tac-toe square values.'''
    CROSS = 1                  # an 'X'
    NAUGHT = 0                  # an 'O'
    EMPTY = -1

    @classmethod
    def cell_str(cls, cell_enum):
        '''Return a string representation of a Cell enum.'''
        if cell_enum == Cell.NAUGHT:
            return 'O'
        elif cell_enum == Cell.CROSS:
            return 'X'
        elif cell_enum == Cell.EMPTY:
            return ' '
    
class InputError(Exception):
    '''Exception raised for errors in the input.
    
    expression -- input expression in which the error occurred
    message -- explanation of the error
    '''

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TicTacToe(object):
    '''A matrix of Cells to represent a tic-tac-toe board.

    :param size: the width and height of the tic-tac-toe board
    '''
    def __init__(self, size=3):
        self.size = size
        self.board = [[Cell.EMPTY for _ in range(self.size)]
                      for _ in range(self.size)]

    def __str__(self):
        build_row = lambda row: [Cell.cell_str(elem) for elem in row]
        row_strings = ['|'.join(build_row(row)) for row in self.board]
        return '\n-+-+-\n'.join(row_strings)

    @property
    def rows(self):
        '''Return a list of all rows in the tic-tac-toe board.'''
        return self.board
        
    @property
    def cols(self):
        '''Return a list of all columns in the tic-tac-toe board.'''
        return zip(*self.rows)

    @property
    def diagonals(self):
        '''Return a list containing the 2 diagonals of the
        tic-tac-toe board.
        '''
        return [[board[i][i] for i in range(self.size)]
                for board in (self.rows,
                              [list(reversed(i)) for i in self.rows])]

    def possible_moves(self):
        '''Return a list of (x,y) tuples that are empty.
        '''
        return [(i,j) for i in range(self.size)
                for j in range(self.size)
                if self.board[i][j] == Cell.EMPTY]
    
    def is_won_by(self, cell):
        '''Return if the given cell enum has won.

        :param cell: -- which Cell enum to check for a win
        '''
        all_match = lambda item: cell == item

        return any([all(all_match, cells) for cells in
                    (self.rows + self.cols + self.diagonals)])
    
    def mark_cell(self, cell, row, col):
        '''Insert cell at (row,col) if it is empty.

        :param cell: the Cell enum to insert
        :param row: which row of the board to insert the cell
        :param col: which col of the board to insert the cell
        '''
        if self.board[row][col] == Cell.EMPTY:
            self.board[row][col] = cell
        else:
            raise InputError(self.board == 1,
                             'Tried to mark a previously marked cell.')
