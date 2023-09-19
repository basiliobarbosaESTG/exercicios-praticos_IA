import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        # tabuleiro e um vencedor definido como nulo
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        # definimos o tabuleiro com 9 espaços
        return [' ' for _ in range(9)]

    def print_board(self):
        # imprimimos 3 rows
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # numeros que correspondem onde o jogador quer jogar(introduzir a "peça")
        # Ou seja, qual o espaço que quer escolher
        # 0 | 1 | 2 |
        # 3 | 4 | 5 |
        # 6 | 7 | 8 |
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # verificamos se o espaço está vazio
        if self.board[square] == ' ':
            # atribuimos a letra ao espaço vazio
            self.board[square] = letter
            # se for o vencedor atribuimos ao jogador atual
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # checkamos a row
        row_ind = math.floor(square / 3)
        # row no tabuleiro
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        # para toda a letra na row é a mesma
        if all([s == letter for s in row]):
            return True
        # checkamos as colunas
        col_ind = square % 3
        # coluna do tabuleiro
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        # para toda a letra na coluna é a mesma
        if all([s == letter for s in column]):
            return True
        # checkamos as diagonais
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # verifica se existem espaços vazio no tabuleiro
    def empty_squares(self):
        return ' ' in self.board
    # conta o numero de espaços vazios

    def num_empty_squares(self):
        return self.board.count(' ')

    # valor numérico dos espaços que ainda estão vazios
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):  # se for uma jogada valida

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()  # criamos uma nova instancia do jogo tictactoe
    # chamamos play no tictactoe usando o x_player e o o_player e imprimimos o jogo(valor true)
    play(t, x_player, o_player, print_game=True)
