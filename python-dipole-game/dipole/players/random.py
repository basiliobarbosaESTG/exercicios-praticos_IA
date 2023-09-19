from random import randint
from random import random ###

from games.dipole.action import DipoleAction
from games.dipole.player import DipolePlayer
from games.dipole.state import DipoleState
from games.state import State


class RandomDipolePlayer(DipolePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DipoleState):
        #row = randint(0, state.get_num_rows())
        #col = randint(0, state.get_num_cols())
        #return DipoleAction(row, col)
        #return DipoleAction(randint(0, state.get_num_cols())) #state.get_num_rows()
        no_moves_left = state.no_valid_moves_left()   
        # Escolha aleatoriamente entre passar e colocar uma peça
        if random() < 0.1 or no_moves_left:  # 10% de chance de passar
            return DipoleAction(-1, -1, True)  # Ação de passar o turno
        else:
            # Tente colocar peças aleatórias até encontrar uma ação válida
            while True:
                action = DipoleAction(randint(0, state.get_num_cols() - 1), randint(0, state.get_num_rows() - 1))
                if state.validate_action(action):
                    return action

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
