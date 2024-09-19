from chessGameInterface import ChessGameInterface, PlayerAlgorithmInterface


class SimpleTicTacToeGUI:
    def __init__(self, game: 'ChessGameInterface', player1: 'PlayerAlgorithmInterface', player2: 'PlayerAlgorithmInterface'):
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

        self.play_game()
    def play_game(self):
        self.game.display_board()

        while True:
            # Player 1's turn
            move = self.player1.make_move(self.game)
            self.game.make_move(move, self.player1.marker)
            self.game.display_board()

            if self.game.check_winner():
                print(f"Player {self.player1.marker} wins!")
                break

            if self.game.is_draw():
                print("It's a draw!")
                break
            input("Press Enter to continue...")
            self.game.switch_player()

            # Player 2's turn
            move = self.player2.make_move(self.game)
            self.game.make_move(move, self.player2.marker)
            self.game.display_board()

            if self.game.check_winner():
                print(f"Player {self.player2.marker} wins!")
                break

            if self.game.is_draw():
                print("It's a draw!")
                break

            self.game.switch_player()
            input("Press Enter to continue...")