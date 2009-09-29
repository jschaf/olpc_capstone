# Frog TicTac - A simple tic tac toe game targeted at the OLPC project

class Cell(object):
    NAUGHT = 1                  # an 'O'
    CROSS = -1                  # an 'X'
    EMPTY = 0


class Board(object):

    def __init__(self):
        self.board = [[Cell.EMPTY for _ in range(3)] for _ in range(3)]

    def __str__(self):
        def toXO(markType):
            if markType == Cell.NAUGHT: return 'O'
            elif markType == Cell.CROSS: return 'X'
            elif markType == Cell.EMPTY: return ' '
            
        rowStrings = ['|'.join(map(toXO, row)) for row in self.board]
        return '\n-+-+-\n'.join(rowStrings)

    
