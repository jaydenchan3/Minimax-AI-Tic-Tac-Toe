# author: Jayden Chan
# date: Feburary 7, 2023
# file: board.py is board class used for tic-tac-toe game
# input: board slot
# output: a tic-tac-toe board

class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ""

    #check_winner for SmartAI
    #gets all possible winning solutions for both self and opponent
    def check_winner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6] # diagonals
        ]
        for position in winning_positions:
            if all(self.board[pos] == 'X' for pos in position):
                self.winner = 'X'
                return self.winner
            if all(self.board[pos] == 'O' for pos in position):
                self.winner = 'O'
                return self.winner
        return ""

    def get_winner(self):
        #checks all winning conditions for X
        if self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
            self.winner = 'X'
        if self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
            self.winner = 'X'
        if self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
            self.winner = 'X'
        if self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
            self.winner = 'X'
        if self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
            self.winner = 'X'
        if self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
            self.winner = 'X'
        if self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
            self.winner = 'X'
        if self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
            self.winner = 'X'

        # checks all winning conditions for O
        if self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
            self.winner = 'O'
        if self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
            self.winner = 'O'
        if self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
            self.winner = 'O'
        if self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
            self.winner = 'O'
        if self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
            self.winner = 'O'
        if self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
            self.winner = 'O'
        if self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
            self.winner = 'O'
        if self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
            self.winner = 'O'
        return self.winner

    # return the winner's sign O or X (an instance winner)
    def set(self, cell, sign):
        tpl = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
        #checks which element in the tuple the input matches, and sets it
        for i in tpl:
            if cell == i:
                self.board[tpl.index(i)] = sign

    # mark the cell on the board with the sign X or O
    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
    # you can use a tuple ("A1", "B1",...) to obtain indexes
    # this implementation is up to you
    def isempty(self, cell):
        tpl = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
        if str(cell) in tpl:
            slot = tpl.index(cell)
            if self.board[slot] == " ": #checks slot the cell on the board to see if it ' '
                return True
        return False

    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
    # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        self.winner = ''
        # check all game terminating conditions, if one of them is present, assign the var done to True
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' ':
            done = True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' ':
            done = True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' ':
            done = True
        elif self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' ':
            done = True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            done = True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ':
            done = True
        elif self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ':
            done = True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            done = True
        #if no winner, checks if all the spots are full
        elif ' ' not in self.board:
            done = True

        return done

    def show(self):
        #prints board and uses list self.board as variables in the slot
        print('\n   A   B   C  ')
        print(' +---+---+---+')
        print(f'1| {self.board[0]} | {self.board[3]} | {self.board[6]} |')
        print(' +---+---+---+')
        print(f'2| {self.board[1]} | {self.board[4]} | {self.board[7]} |')
        print(' +---+---+---+')
        print(f'3| {self.board[2]} | {self.board[5]} | {self.board[8]} |')
        print(' +---+---+---+')
