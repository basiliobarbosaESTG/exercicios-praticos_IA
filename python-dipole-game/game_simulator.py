from abc import ABC, abstractmethod

from games.player import Player
from games.state import State


class GameSimulator(ABC):  # herda da classe ABC(Abstract Base Class)

    def __init__(self, players: list):  # recebe a lista de jogadores
        # only allow list of players
        assert len(
            list(filter(lambda p: not isinstance(p, Player), players))) <= 0

        # stores the possible permutations between players
        self.__permutations = []  # Lista de permutações, onde são guardadas as permutações

        self.heap_permutation(players, len(players))

        # the selected permutation for the current game
        self.__current_permutation = 0

    """
    Adapted from https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/
    It allows for generating all possible permutations of seats in a game
    """

    # algoritmo recursivo que permite gerar todas as permutacoes possíveis de n objetos
    # Método que gera todas as permutações possíveis da lista de jogadores
    # a é uma lista que contem elementos para ser permutados e size - tamanho da lista
    def heap_permutation(self, a: list, size: int):
        # A função verifica se o tamanho da lista é 1, o que indica que uma permutação foi gerada
        if size == 1:  # imprime a permutacao obtida
            # anexamos a lista a.copy() copiando o seu conteúdo
            # que guarda todas as permutacoes possiveis na lista (__permutations) através do metodo append()
            self.__permutations.append(a.copy())

        for i in range(0, size):
            # A função percorre os elementos na lista e chama a si mesma recursivamente com um tamanho de lista menor (size-1).
            self.heap_permutation(a, size - 1)

            # troca elementos na lista para gerar novas permutações
            # Se o tamanho da lista for ímpar, o primeiro elemento é trocado pelo último elemento.
            if size % 2 == 1:
                temp = a[0]
                a[0] = a[size - 1]
                a[size - 1] = temp
            # Se o tamanho da lista for par, o elemento atual é trocado pelo último elemento
            else:
                temp = a[i]
                a[i] = a[size - 1]
                a[size - 1] = temp

    """
    Swaps the order of the players. The order is changed in a way that guarantees that all combinations are considered
    Example for 2 players [a,b]
        - iteration 1: a,b
        - iteration 2, b,a
        - iteration 3, a,b (back to the initial configuration)
    """

    # Funcao/Método que muda as posições dos jogadores para a próxima permutação
    def change_player_positions(self):
        self.__current_permutation += 1
        if self.__current_permutation >= len(self.__permutations):
            self.__current_permutation = 0

    # Os métodos para executar um jogo são abstratos,
    # o que significa que não são implementados na classe GameSimulator,
    # mas devem ser implementados em classes derivadas que herdam dela.

    """
    starts a new game
    """

    @abstractmethod
    def init_game(self) -> State:
        pass

    """
    event before a game ends
    """

    @abstractmethod
    def before_end_game(self, state):
        pass

    """
    event when a game ends
    """

    @abstractmethod
    def end_game(self, state):
        pass

    """
    """

    def get_player_positions(self):
        return self.__permutations[self.__current_permutation]

    """
    runs the simulation
    """

    # inicializa o estado do jogo e as posições dos jogadores,
    # notifica os jogadores que um novo jogo está a começar,
    # é obtida a ação de cada jogador até que o jogo termine
    # e então notifica os jogadores sobre o resultado do jogo
    def run_simulation(self):
        state = self.init_game()
        players = self.get_player_positions()

        # notify players a new game is starting
        for pos in range(0, len(players)):
            players[pos].set_current_pos(pos)
            players[pos].event_new_game()

        # play a turn
        while not state.is_finished():
            selected_action = None
            pos = state.get_acting_player()

            # obtain a valid action
            while True:
                selected_action = players[pos].get_action(state.clone())
                if state.validate_action(selected_action):
                    break

            state.play(selected_action)

            # notify players of the action
            for player in players:
                player.event_action(pos, selected_action, state.clone())

        # handler to run before the game ends
        self.before_end_game(state)

        # notify all players of the result each player got
        for player in players:
            for pos in range(0, len(players)):
                player.event_result(pos, state.get_result(pos))
            player.event_end_game(state.clone())

        # handler to run after a game ends
        self.end_game(state)

    # prints the stats for all players
    def print_stats(self):
        for player in self.__permutations[0]:
            player.print_stats()

    # returns the list of players
    def get_players(self):
        return self.__permutations[0]

    # returns the ordered list of players for the current permutation
    # retorna a lista ordenada de jogadores para a permutação atual
    def get_player_positions(self):
        return self.__permutations[self.__current_permutation]

    # gets the number os players
    def num_players(self):
        return len(self.__permutations[0])
