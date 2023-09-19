from abc import ABC

from games.dipole.result import DipoleResult
from games.player import Player


# classe filha de Player e ABC, ou seja, DipolePlayer herda de Player e ABC
class DipolePlayer(Player, ABC):

    def __init__(self, name):
        super().__init__(name)

        """
        stats is a dictionary that will store the number of times each result occurred
        """
        self.__stats = {}
        # implementa a classe DipoleResult que é o enum do resultado do jogo
        for dipoleRes in DipoleResult:
            self.__stats[dipoleRes] = 0

        """
        here we are storing the number of games
        """
        self.__num_games = 0

    # imprime estatisticas do jogador, como o numero de vitorias e a taxa de vitorias
    def print_stats(self):
        num_wins = self.__stats[DipoleResult.WIN]
        print(
            f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({num_wins * 100.0 / self.__num_games} win "
            f"rate)")

    def event_new_game(self):
        self.__num_games += 1

    # atualiza as estatisticas do jogador quando o jogo termina
    def event_result(self, pos: int, result: DipoleResult):
        if pos == self.get_current_pos():
            self.__stats[result] += 1
