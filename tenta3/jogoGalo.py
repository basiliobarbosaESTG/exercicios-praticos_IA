import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# Decide que jogador vai jogar primeiro
turno = 0

# Cria um tabuleiro vazio
global tabuleiro  # lista de listas que armazena todos os quadrados do tabuleiro
tabuleiro = [[" " for x in range(3)]
             for y in range(3)]  # com 3 linhas e 3 colunas

# Check l(O/X) won the match or not
# according to the rules of the game


def vencedor(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


def obter_texto(i, j, gb, l1, l2):  # Configura o texto no botão ao jogar com outro jogador
    # i e j são as coordenadas do butão que estamos a clicar
    global turno
    # caso esteja vazio apenas será possível introduzir uma "peça" para cada jogador - X e O
    if tabuleiro[i][j] == ' ':
        if turno % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            tabuleiro[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            tabuleiro[i][j] = "O"
        turno += 1
        button[i][j].config(text=tabuleiro[i][j])
    if vencedor(tabuleiro, "X"):  # quando o "X" vence
        # global board
        gb.destroy()
        box = messagebox.showinfo("Vencedor", "Jogador 1 ganhou o jogo")
    elif vencedor(tabuleiro, "O"):  # quando o "O" vence
        gb.destroy()
        box = messagebox.showinfo("Vencedor", "Jogador 2 ganhou o jogo")
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("Jogo Empatado", "Jogo Empatado")


def isfree(i, j):  # verifica se o jogador pode apertar o botão, caso não possa motrará uma mensagem de erro e destruirá o tabuleiro
    return tabuleiro[i][j] == " "


def isfull():  # Verifica se o tabuleiro está cheio, ou seja, se existem células preenchidas no jogo
    flag = True  # significa que não há espaços no tabuleiro e continuará a verificar até encontrar um espaço vazio
    for i in tabuleiro:
        if (i.count(' ') > 0):
            flag = False
    return flag


# Cria a GUI do jogo de tabuleiro para jogar com outro jogador
def jogoTabuleiroPlayer(jogo_tabuleiro, l1, l2):
    # l1 e l2 representam os butões que estão atualmente ativos no jogo
    global button  # lista de listas que armazena todos os botoes em ordem
    button = []  # lista de butões(1 "não funcional" e 3 "clicáveis")
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(obter_texto, i, j, jogo_tabuleiro, l1, l2)
            button[i][j] = Button(
                jogo_tabuleiro, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    jogo_tabuleiro.mainloop()


def pc():  # Decide a próxima jogada do computador, escolhendo-a aleatoriamente(move) das jogadas possiveis(possiblemoves)
    possiblemove = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                tabuleiroPC = deepcopy(tabuleiro)
                tabuleiroPC[i[0]][i[1]] = let
                if vencedor(tabuleiroPC, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]


# Configura/determina o texto que vai ser mostrado no botão ao jogar com o computador
def obter_texto_pc(i, j, gb, l1, l2):
    global turno
    if tabuleiro[i][j] == ' ':
        if turno % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            tabuleiro[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            tabuleiro[i][j] = "O"
        turno += 1
        button[i][j].config(text=tabuleiro[i][j])
    x = True
    if vencedor(tabuleiro, "X"):
        # global board
        gb.destroy()
        x = False
        box = messagebox.showinfo("Vencedor", "Jogador ganhou a partida")
    elif vencedor(tabuleiro, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Vencedor", "Computador ganhou a partida")
    elif (isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Jogo Empatado", "Jogo Empatado")
    if (x):
        if turno % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            obter_texto_pc(move[0], move[1], gb, l1, l2)


# Cria a interface do jogo de tabuleiro para jogar com o computador
def jogoTabuleiroPC(jogo_tabuleiro, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(obter_texto_pc, i, j, jogo_tabuleiro, l1, l2)
            button[i][j] = Button(
                jogo_tabuleiro, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    jogo_tabuleiro.mainloop()


def jogaComPC(jogo_tabuleiro):  # Inicializa o jogo de tabuleiro para jogar com o computador
    jogo_tabuleiro.destroy()
    jogo_tabuleiro = Tk()
    jogo_tabuleiro.title("Tic Tac Toe")
    l1 = Button(jogo_tabuleiro, text="Jogador : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(jogo_tabuleiro, text="Computador : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    jogoTabuleiroPC(jogo_tabuleiro, l1, l2)


# Inicializa o jogo de tabuleiro para jogar com outro jogador
def jogaComJogador(jogo_tabuleiro):
    jogo_tabuleiro.destroy()
    jogo_tabuleiro = Tk()
    jogo_tabuleiro.title("Tic Tac Toe")
    l1 = Button(jogo_tabuleiro, text="Jogador 1 : X", width=10)

    l1.grid(row=1, column=1)
    l2 = Button(jogo_tabuleiro, text="Jogador 2 : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    jogoTabuleiroPlayer(jogo_tabuleiro, l1, l2)


def play():  # Função main
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Jogo do galo")
    wpc = partial(jogaComPC, menu)
    wpl = partial(jogaComJogador, menu)

    head = Button(menu, text="---Bem-vindo ao jogo do galo---",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=5)

    B1 = Button(menu, text="Single Player", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)

    B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)

    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Chama a função main
if __name__ == '__main__':
    play()
