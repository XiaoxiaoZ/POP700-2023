from typing import Dict, List
from chessGameInterface import ChessGameInterface


class TicTacToeGame(ChessGameInterface):
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|".join(row))
            print("-" * 5)
        print("\n")

    def is_valid_move(self, position):
        # need updates
        return 0 <= position < 9 and self.board[position] == ' '

    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]  # Return the winner ('X' or 'O')
        return None

    def is_draw(self):
        return ' ' not in self.board

    def reset_board(self):
        self.board = [' ' for _ in range(9)]

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_game_state(self) -> List[List[str]]:
        """Returns the current game state as a 2D list.
        # Get the game state in 2D list format
        print("2D List Game State:")
        print(game.get_game_state())  # ['X', ' ', ' ',' ', 'O', ' ', ' ', ' ', ' ']
        """
        return self.board

    def get_game_state_dict(self) -> Dict[int, str]:
        """Returns the current game state as a dictionary mapping positions to players.
        # Get the game state as a dictionary
        print("Dictionary Game State:")
        print(game.get_game_state_dict())  # {0: 'X', 1: ' ', 2: ' ', 3: ' ', 4: 'O', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
        """
        return {i: self.board[i] for i in range(9)}