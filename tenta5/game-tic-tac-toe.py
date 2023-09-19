import random
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.backend import reshape
from keras.utils.np_utils import to_categorical

# Get an empty board
#
# 0 indicates an empty space, 1 indicates an 'X' (player 1), and 2 indicates an 'O' (player 2)
#
# Initially the board is empty, so we return a 3x3 array of zeroes.


def initBoard():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return board

# Print the current state of the board


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            mark = ' '
            if board[i][j] == 1:
                mark = 'X'
            elif board[i][j] == 2:
                mark = 'O'
            if (j == len(board[i]) - 1):
                print(mark)
            else:
                print(str(mark) + "|", end='')
        if (i < len(board) - 1):
            print("-----")

# Get a list of valid moves (indices into the board)


def getMoves(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves

# Declare a winner
#
# -1 = game not over
#  0 = draw
#  1 = 'X' wins (player 1)
#  2 = 'O' wins (player 2)


def getWinner(board):
    candidate = 0
    won = 0

    # Check rows
    for i in range(len(board)):
        candidate = 0
        for j in range(len(board[i])):

            # Make sure there are no gaps
            if board[i][j] == 0:
                break

            # Identify the front-runner
            if candidate == 0:
                candidate = board[i][j]

            # Determine whether the front-runner has all the slots
            if candidate != board[i][j]:
                break
            elif j == len(board[i]) - 1:
                won = candidate

    if won > 0:
        return won

    # Check columns
    for j in range(len(board[0])):
        candidate = 0
        for i in range(len(board)):

            # Make sure there are no gaps
            if board[i][j] == 0:
                break

            # Identify the front-runner
            if candidate == 0:
                candidate = board[i][j]

            # Determine whether the front-runner has all the slots
            if candidate != board[i][j]:
                break
            elif i == len(board) - 1:
                won = candidate

    if won > 0:
        return won

    # Check diagonals
    candidate = 0
    for i in range(len(board)):
        if board[i][i] == 0:
            break
        if candidate == 0:
            candidate = board[i][i]
        if candidate != board[i][i]:
            break
        elif i == len(board) - 1:
            won = candidate

    if won > 0:
        return won

    candidate = 0
    for i in range(len(board)):
        if board[i][2 - i] == 0:
            break
        if candidate == 0:
            candidate = board[i][2 - i]
        if candidate != board[i][2 - i]:
            break
        elif i == len(board) - 1:
            won = candidate

    if won > 0:
        return won

    # Still no winner?
    if (len(getMoves(board)) == 0):
        # It's a draw
        return 0
    else:
        # Still more moves to make
        return -1


    # Test helper methods
b = initBoard()
printBoard(b)
print(getWinner(b))
print(getMoves(b))

b[0][0] = 1
b[1][1] = 1
b[2][2] = 1
printBoard(b)
print(getWinner(b))

b[0][2] = 2
b[1][2] = 2
b[2][2] = 2
printBoard(b)
print(getWinner(b))

b[0][1] = 1
b[1][0] = 2
b[2][0] = 1
b[2][1] = 2
b[2][2] = 1
b[0][0] = 2
printBoard(b)
print(getWinner(b))

random.seed()

# Get best next move for the given player at the given board position


def bestMove(board, model, player, rnd=0):
    scores = []
    moves = getMoves(board)

    # Make predictions for each possible move
    for i in range(len(moves)):
        future = np.array(board)
        future[moves[i][0]][moves[i][1]] = player
        prediction = model.predict(future.reshape((-1, 9)), verbose=0)[0]
        if player == 1:
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
        else:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        drawPrediction = prediction[0]
        if winPrediction - lossPrediction > 0:
            scores.append(winPrediction - lossPrediction)
        else:
            scores.append(drawPrediction - lossPrediction)

    # Choose the best move with a random factor
    bestMoves = np.flip(np.argsort(scores))
    for i in range(len(bestMoves)):
        if random.random() * rnd < 0.5:
            return moves[bestMoves[i]]

    # Choose a move completely at random
    return moves[random.randint(0, len(moves) - 1)]

# Simulate a game


def simulateGame(p1=None, p2=None, rnd=0):
    history = []
    board = initBoard()
    playerToMove = 1

    while getWinner(board) == -1:

        # Chose a move (random or use a player model if provided)
        move = None
        if playerToMove == 1 and p1 != None:
            move = bestMove(board, p1, playerToMove, rnd)
        elif playerToMove == 2 and p2 != None:
            move = bestMove(board, p2, playerToMove, rnd)
        else:
            moves = getMoves(board)
            move = moves[random.randint(0, len(moves) - 1)]

        # Make the move
        board[move[0]][move[1]] = playerToMove

        # Add the move to the history
        history.append((playerToMove, move))

        # Switch the active player
        playerToMove = 1 if playerToMove == 2 else 2

    return history


# Simulate a game
history = simulateGame()
print(history)

# Reconstruct the board from the move list


def movesToBoard(moves):
    board = initBoard()
    for move in moves:
        player = move[0]
        coords = move[1]
        board[coords[0]][coords[1]] = player
    return board


board = movesToBoard(history)
printBoard(board)
print(getWinner(board))

games = [simulateGame() for _ in range(10000)]

# Aggregate win/loss/draw stats for a player


def gameStats(games, player=1):
    stats = {"win": 0, "loss": 0, "draw": 0}
    for game in games:
        result = getWinner(movesToBoard(game))
        if result == -1:
            continue
        elif result == player:
            stats["win"] += 1
        elif result == 0:
            stats["draw"] += 1
        else:
            stats["loss"] += 1

    winPct = stats["win"] / len(games) * 100
    lossPct = stats["loss"] / len(games) * 100
    drawPct = stats["draw"] / len(games) * 100

    print("Results for player %d:" % (player))
    print("Wins: %d (%.1f%%)" % (stats["win"], winPct))
    print("Loss: %d (%.1f%%)" % (stats["loss"], lossPct))
    print("Draw: %d (%.1f%%)" % (stats["draw"], drawPct))


gameStats(games)
print()
gameStats(games, player=2)


def getModel():
    numCells = 9  # How many cells in a 3x3 tic-tac-toe board?
    # How many outcomes are there in a game? (draw, X-wins, O-wins)
    outcomes = 3
    model = Sequential()
    model.add(Dense(200, activation='relu', input_shape=(9, )))
    model.add(Dropout(0.2))
    model.add(Dense(125, activation='relu'))
    model.add(Dense(75, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(outcomes, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop', metrics=['acc'])
    return model


model = getModel()
print(model.summary())

# Get a set of board states labelled by who eventually won that game


def gamesToWinLossData(games):
    X = []
    y = []
    for game in games:
        winner = getWinner(movesToBoard(game))
        for move in range(len(game)):
            X.append(movesToBoard(game[:(move + 1)]))
            y.append(winner)

    X = np.array(X).reshape((-1, 9))
    y = to_categorical(y)

    # Return an appropriate train/test split
    trainNum = int(len(X) * 0.8)
    return (X[:trainNum], X[trainNum:], y[:trainNum], y[trainNum:])


# Split out train and validation data
X_train, X_test, y_train, y_test = gamesToWinLossData(games)

nEpochs = 100
batchSize = 100
history = model.fit(X_train, y_train, validation_data=(
    X_test, y_test), epochs=nEpochs, batch_size=batchSize)

games2 = [simulateGame(p1=model) for _ in range(1000)]
gameStats(games2)

games3 = [simulateGame(p2=model) for _ in range(1000)]
gameStats(games3, player=2)

games4 = [simulateGame(p1=model, p2=model, rnd=0.6) for _ in range(1000)]
gameStats(games4, player=1)
print()
gameStats(games4, player=2)

print("Average length of fully random game is %f moves" %
      (np.mean([float(len(game)) for game in games])))
print("Average length of game where P1 uses NN is %f moves" %
      (np.mean([float(len(game)) for game in games2])))
print("Average length of game where P2 uses NN is %f moves" %
      (np.mean([float(len(game)) for game in games3])))
print("Average length of game where both use NN is %f moves" %
      (np.mean([float(len(game)) for game in games4])))

# Create new board
board = initBoard()

# Move 1 (computer)
move = bestMove(board, model, 1)
board[move[0]][move[1]] = 1
printBoard(board)

# Move 2 (human)
board[1][1] = 2
printBoard(board)

# Move 3 (computer)
move = bestMove(board, model, 1)
board[move[0]][move[1]] = 1
printBoard(board)

# Move 4 (human)
board[0][2] = 2
printBoard(board)

# Move 5 (computer)
move = bestMove(board, model, 1)
board[move[0]][move[1]] = 1
printBoard(board)

# Move 6 (human)
board[2][1] = 2
printBoard(board)

# Move 7 (computer)
move = bestMove(board, model, 1)
board[move[0]][move[1]] = 1
printBoard(board)
