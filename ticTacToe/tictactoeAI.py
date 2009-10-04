''' TicTacToeAI - a collection of various AIs for tic-tac-toe.

* Win: If you have two in a row, play the third to get three in a row.

* Block: If the opponent has two in a row, play the third to block
  them.

* Fork: Create an opportunity where you can win in two ways.

* Block Opponent's Fork:

    Option 1
    
       Create two in a row to force the opponent into defending, as
       long as it doesn't result in them creating a fork or
       winning. For example, if "X" has a corner, "O" has the center,
       and "X" has the opposite corner as well, "O" must not play a
       corner in order to win. (Playing a corner in this scenario
       creates a fork for "X" to win.)

    Option 2

        If there is a configuration where the opponent can fork, block
        that fork.

* Center: Play the center.

* Opposite Corner: If the opponent is in the corner, play the opposite corner.

* Empty Corner: Play an empty corner.

* Empty Side: Play an empty side.

'''
import abc
from frog_naught import TicTacToe, Cell
import itertools as itools

class TicTacToeAI(object):
    __metaclass__ = abc.ABCMeta

    def find_win_spot(self, board, cell):
        for a,b,c in (board.rows + board.cols + board.diagonals):
            if cell == a == b or cell == b == c or cell == a == c:
                pass
            
    def find_block_spot(self, board, cell):
        opposite = Cell.CROSS if cell == Cell.NAUGHT else Cell.NAUGHT
        return find_win_spot(self, board, opposite)



        
    @abc.abstractmethod
    def make_move(self, board):
        pass
    
    
class PerfectAI(TicTacToeAI):
    '''
    '''
    def __init__(self, cell):
        self.cell = cell
        
    def make_move(self, board):
        
        
        
    
