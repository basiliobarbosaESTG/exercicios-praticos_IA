from games.dipole.player import DipolePlayer
from games.dipole.state import DipoleState
from games.game_simulator import GameSimulator


class DipoleSimulator(GameSimulator):
    # INICIALIZA COM 2 JOGADORES
    # DEFINIR NUMER0 DE ROWS E COLS PARA O TABULEIRO DIPOLE - "DESENHAR O TABULEIRO"
    def __init__(self, player1: DipolePlayer, player2: DipolePlayer, num_rows: int = 8, num_cols: int = 8): ###
        super(DipoleSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the Dipole grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols ###

    def init_game(self):
        return DipoleState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: DipoleState):
        # ignored for this simulator
        pass

    def end_game(self, state: DipoleState):
        # ignored for this simulator
        pass
