import matplotlib.pyplot as plt

plt.plot([i**2 for i in range(10)])
plt.show()

### Homework 2 ###
# Exercise 1
'''
Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two
players take turns placing a mark on a 3x3 board, attempting to make a row,
column, or diagonal of three with their mark. In this homework, we will use
the tools we've covered in the past two weeks to create a tic-tac-toe simulator
and evaluate basic winning strategies.
In the following 13 exercises, we will learn to create a tic-tac-toe board,
place markers on the board, evaluate if either player has won, and use this to
simulate two basic strategies.
'''

import numpy as np

# Exercise 1
# For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3.
# Make a function create_board() that creates such a board, with values of integers 0.
# Call create_board(), and store this as board.
def create_board():
    return np.zeros((3,3))

board = create_board()

# Exercise 2
# Create a function place(board, player, position), where:
# player is the current player (an integer 1 or 2)
# position a tuple of length 2 specifying a desired location to place their marker.
# Your function should only allow the current player to place a marker on the board (change the board position to their number) if that position is empty (zero).
# Use create_board() to store a board as board, and use place to have Player 1 place a marker on location (0, 0).
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

board = create_board()
place(board, 1, (0,0))

# Exercise 3
# Create a function possibilities(board) that returns a list of all positions (tuples) on the board that are not occupied (0). (Hint: numpy.where is a handy function that returns a list of indices that meet a condition.)
# board is already defined from previous exercises. Call possibilities(board) to see what it returns!
def possibilities(board):
    return list(zip(*np.where(board == 0))) # Tell me Why by Demigodz 🎶

possibilities(board)

# Exercise 4
# Write a function random_place(board, player) that places a marker for the current player at random among all the available positions (those currently set to 0).
# Find possible placements with possibilities(board).
# Select one possible placement at random using random.choice(selection).
# board is already defined from previous exercises. Call random_place(board, player) to place a random marker for Player 2, and store this as board to update its value.
import random
def random_place(board, player):
    empty_cells = possibilities(board)
    place(board, player, random.choice(empty_cells))

random_place(board, 2)

# Exercise 5
# board is already given. Call random_place(board, player) to place three pieces each on board for players 1 and 2.
# Print board to see your result.
board = create_board()

for i in range(3):
    random_place(board, 1)
    random_place(board, 2)

print(board)

# Exercise 6
# Make a function row_win(board, player) that takes the player (integer), and determines if any row consists of only their marker. Have it return True of this condition is met, and False otherwise.
# board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.
def row_win(board, player):
    for row in board:
        for i in row:
            if i != player:
                return False
            return True

row_win(board, 1)
'''
alternatively, you can use following:

def row_win(board, player):
    if np.any(np.all(board == player, axis = 1)):
        return True
    else:
        return False

or even shorter:

def row_win(board, player):
    return np.any(np.all(board == player, axis = 1))
'''

# Exercise 7
# Create a similar function col_win(board, player) that takes the player (integer), and determines if any column consists of only their marker. Have it return True if this condition is met, and False otherwise.
# board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.
def col_win(board, player):
    for col in board.transpose():
        for i in col:
            if i != player:
                return False
            return True

col_win(board, 1)
'''
alternatively, you can use following:

def col_win(board, player):
    if np.any(np.all(board == player, axis = 0)):
        return True
    else:
        return False

or even shorter:

def col_win(board, player):
    return np.any(np.all(board == player, axis = 0))
'''

# Exercise 8
# Finally, create a function diag_win(board, player) that tests if either diagonal of the board consists of only their marker. Have it return True if this condition is met, and False otherwise.
# board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.
def diag_win(board, player):
    for i in range(len(board)):
        if board[(i, i)] != player:
            return False
        return True

diag_win(board, 1)

'''
some PyMagic here:

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        return True
    else:
        return False

and BLACK PyMagic:

def diag_win(board, player):
    return np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player)
'''
# Exercise 9
# Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players. If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
# board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

# Exercise 10
# create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. Create a function play_game() that:
# Creates a board.
# Alternates taking turns between two players (beginning with Player 1), placing a marker during each turn.
# Evaluates the board for a winner after each placement.
# Continues the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
# Call play_game once.
def play_game():
    board = create_board()
    while len(possibilities(board)):
        random_place(board, 1)
        random_place(board, 2)
        if evaluate(board) == 0:
            pass
        else:
            return evaluate(board)

play_game()

'''
or the right way:

def play_game():
    board, winner = create_board(), 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
'''

# Exercise 11
# Use the play_game() function to play 1,000 random games, where Player 1 always goes first.
# Import and use the time library to call the time() function both before and after playing all 1,000 games.
# Store these times as start and stop, respectively.
# Subtract them to evaluate how long it takes to play 1,000 games, and print your answer.
# The library matplotlib.pyplot has already been stored as plt. Use plt.hist() and plt.show() to plot a histogram of the results.
# Does Player 1 win more than Player 2?
# Does either player win more than each player draws?
import time
start = time.time()

res = []
for i in range(1000):
    res.append(play_game())

stop = time.time()

print(stop - start)

plt.hist(res)
plt.show()

# Exercise 12
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game()

# Exercise 13
# write your code here!
import time
start = time.time()
res = []
for i in range(1000):
    res.append(play_strategic_game())
stop = time.time()
print(stop - start)

plt.hist(res)
plt.show()
