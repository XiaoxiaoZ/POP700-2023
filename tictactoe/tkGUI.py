
import tkinter as tk
from tkinter import messagebox  
from typing import List

from chessGameInterface import ChessGameInterface, PlayerAlgorithmInterface
from defaultAlgorithm import MinimaxAlgorithm, RandomAlgorithm
from tictactoeGame import TicTacToeGame

class TicTacToeGUI:
    def __init__(self, root: tk.Tk, game: 'ChessGameInterface', player1: 'PlayerAlgorithmInterface', player2: 'PlayerAlgorithmInterface'):
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

        self.buttons = []
        self.create_widgets(root)
        self.play_game()

    def create_widgets(self, root: tk.Tk):
        """Creates the game board with labels."""
        for i in range(3):
            row = []
            for j in range(3):
                label = tk.Label(root, text='', font=('Arial', 24), width=5, height=2,
                                 borderwidth=1, relief='solid')
                label.grid(row=i, column=j)
                row.append(label)
            self.buttons.append(row)

    def update_board(self):
        """Updates the GUI with the current game state."""
        state = self.game.get_game_state_dict()
        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[row][col].config(text=state[i] if state[i] != ' ' else '')

    def check_end_conditions(self):
        """Checks for game end conditions and updates the GUI accordingly."""
        winner = self.game.check_winner()
        if winner:
            tk.messagebox.showinfo("Game Over", f"{winner} wins!")
            return True
        elif self.game.is_draw():
            tk.messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def play_game(self):
        """Runs the game loop, making moves and updating the GUI."""
        while not self.check_end_conditions():
            move = self.current_player.make_move(self.game)
            self.game.make_move(move, self.current_player.marker)
            self.update_board()
            input("Press Enter to continue...")
            # Switch players
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1

def play_game():
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Create the game and players
    game = TicTacToeGame()
    player1 = MinimaxAlgorithm('X')  # Replace with your desired algorithm
    player2 = RandomAlgorithm('O')  # Replace with your desired algorithm

    # Set up the GUI
    gui = TicTacToeGUI(root, game, player1, player2)

    # Start the GUI loop
    root.mainloop()

# Call play_game to start the game
play_game()