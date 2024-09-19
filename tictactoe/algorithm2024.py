from chessGameInterface import ChessGameInterface, PlayerAlgorithmInterface


class StupidAlgorithm(PlayerAlgorithmInterface):

    def __init__(self, marker: str): ## not needed

        super().__init__(marker)

        self.opponent_marker = 'O' if marker == 'X' else 'X'

        

    def make_move(self,game:'ChessGameInterface') -> int:

        board=game.get_game_state()

        for i in range(9):

            if board[i]==' ':

                return i 
