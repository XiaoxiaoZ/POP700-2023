from typing import List, Dict, Optional
from defaultAlgorithm import HumanPlayer, MinimaxAlgorithm, RandomAlgorithm
from defaultGUI import SimpleTicTacToeGUI
from algorithm2024 import StupidAlgorithm
from tictactoeGame import TicTacToeGame


player1 = MinimaxAlgorithm('X')  # Replace with your desired algorithm
player2 = StupidAlgorithm('O')  # Replace with your desired algorithm

# Set up the GUI
simpleGUI = SimpleTicTacToeGUI(TicTacToeGame(), player1, player2)

