from chessGameInterface import PlayerAlgorithmInterface, ChessGameInterface

import random

from typing import List


class RandomAlgorithm(PlayerAlgorithmInterface):
    def make_move(self, game: ChessGameInterface):
        available_moves = [i for i in range(9) if game.is_valid_move(i)]
        return random.choice(available_moves)

class HumanPlayer(PlayerAlgorithmInterface):
    def make_move(self, game: ChessGameInterface):
        while True:
            try:
                move = int(input(f"Player {self.marker}, enter your move (0-8): "))
                if game.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

class MinimaxAlgorithm(PlayerAlgorithmInterface):
    def __init__(self, marker: str):
        super().__init__(marker)
        self.opponent_marker = 'O' if marker == 'X' else 'X'

    def evaluate(self, board: List[str]) -> int:
        """Evaluates the board and returns a score."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]

        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
                if board[condition[0]] == self.marker:
                    return 10
                elif board[condition[0]] == self.opponent_marker:
                    return -10

        return 0

    def minimax(self, board: List[str], depth: int, is_max: bool) -> int:
        """Minimax recursive algorithm."""
        score = self.evaluate(board)

        if score == 10 or score == -10:
            return score

        if ' ' not in board:
            return 0

        if is_max:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.marker
                    best_score = max(best_score, self.minimax(board, depth + 1, False))
                    board[i] = ' '
            return best_score

        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.opponent_marker
                    best_score = min(best_score, self.minimax(board, depth + 1, True))
                    board[i] = ' '
            return best_score

    def make_move(self, game: 'ChessGameInterface') -> int:
        """Determines the best move using the Minimax algorithm."""
        best_value = -float('inf')
        best_move = -1
        board = game.get_game_state()
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.marker
                move_value = self.minimax(game.board, 0, False)
                board[i] = ' '
                
                if move_value > best_value:
                    best_move = i
                    best_value = move_value

        return best_move