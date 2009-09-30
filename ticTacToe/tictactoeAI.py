''' TicTacToeAI - a collection of various AIs for tic-tac-toe.

'''
import abc
from frog_naught import TicTacToe

class TicTacToeAI(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next_move(self, board):
        pass

class PerfectAI(TicTacToeAI):
    '''
    '''
    def __init__(self, cell):
        self.cell = cell
        
    def next_move(self, board):
        
        
        
    
