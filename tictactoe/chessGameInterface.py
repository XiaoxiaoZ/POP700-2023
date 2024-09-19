from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class ChessGameInterface(ABC):
    @abstractmethod
    def is_valid_move(self, position: int) -> bool:
        """Checks if a given move is valid."""
        pass

    @abstractmethod
    def make_move(self, position: int, player: str) -> bool:
        """Makes a move on the board for the given player."""
        pass

    @abstractmethod
    def check_winner(self) -> Optional[str]:
        """Checks if there is a winner, returns 'X', 'O', or None."""
        pass

    @abstractmethod
    def is_draw(self) -> bool:
        """Checks if the game is a draw (no more valid moves)."""
        pass

    @abstractmethod
    def reset_board(self) -> None:
        """Resets the game board for a new game."""
        pass

    @abstractmethod
    def switch_player(self) -> None:
        """Switches the current player between 'X' and 'O'."""
        pass

    @abstractmethod
    def get_game_state(self) -> List[List[str]]:
        """Returns the current game state as a 2D list of strings."""
        pass

    @abstractmethod
    def get_game_state_dict(self) -> Dict[int, str]:
        """Returns the current game state as a dictionary mapping positions to players."""
        pass

class PlayerAlgorithmInterface(ABC):
    def __init__(self, marker):
        """Initializes the player with their marker ('X' or 'O')."""
        self.marker = marker

    @abstractmethod
    def make_move(self, game: ChessGameInterface):
        """Determines the next move for the player.
        
        Args:
            game (TicTacToeInterface): The current game state.
        
        Returns:
            int: The position (0-8) where the player will place their marker.
        """
        pass