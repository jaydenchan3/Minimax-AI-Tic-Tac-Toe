# author: Jayden Chan
# date: Feburary 7, 2023
# file: player.py is board class used for tic-tac-toe game
# input: board slot
# output: player choice onto board

import random


class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        return self.sign

    # return an instance sign
    def get_name(self):
        return self.name

    # return an instance name
    def choose(self, board):
        tpl = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
        while True:
            # trys to get input and place it onto the board
            try:
                cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n')
                if board.isempty(cell.upper()) and cell.upper() in tpl:
                    board.set(cell.upper(), self.sign)
                    break
                # asks it to choose again if it inputs an invalid input
                else:
                    print('You did not choose correctly.')
            except:
                print('You did not choose correctly.')


# prompt the user to choose a cell
# if the user enters a valid string and the cell on the board is empty, update the board
# otherwise print a message that the input is wrong and rewrite the prompt
# use the methods board.isempty(cell), and board.set(cell, sign)

class AI(Player):
    def __init__(self, name, sign, board):
        Player.__init__(self, name, sign)
        self.board = board

    def choose(self, board):
        tpl = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
        while True:
            # gets random cell and sets it into the board
            cell = random.choice(tpl)
            if board.isempty(cell):
                board.set(cell, self.sign)
                break


class MiniMax(AI):

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # self is a loser (opponent is a winner)
            elif board.get_winner() == '':
                return 0
            # is a tie
            else:
                return -1
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code

        else:
            # assign min and max
            min_score = float('inf')
            max_score = float('-inf')
            # assign sign and other player's sign
            if self.sign == 'O':
                other_sign = 'X'
            else:
                other_sign = 'O'

            for cell in ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'):
                if board.isempty(cell):
                    if self_player:
                        board.set(cell, self.sign)
                    else:
                        board.set(cell, other_sign)
                    score = MiniMax.minimax(self, board, not self_player, False)  # use recursion to get score
                    board.set(cell, ' ')  # reset board
                    if score > max_score and self_player:  # sets max_score and cell
                        max_score = score
                        max_cell = cell
                    elif score < min_score and not self_player:  # sets min_score
                        min_score = score
            if start:
                return max_cell
            elif self_player:
                return max_score
            else:
                return min_score


class SmartAI(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)

    def choose(self, board):
        # Check if AI can win in one move
        tpl = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        if self.sign == 'O':
            other_sign = 'X'
        else:
            other_sign = 'O'

        for cell in tpl:
            if board.isempty(cell):
                board.set(cell, self.sign)
                if board.check_winner() == self.sign:
                    board.set(cell, ' ')
                    board.set(cell, self.sign)
                    return (cell)
                board.set(cell, ' ')

            # Check if opponent can win in one move
        for cell in tpl:
            if board.isempty(cell):
                board.set(cell, other_sign)
                if board.check_winner() == other_sign:
                    board.set(cell, ' ')
                    board.set(cell, self.sign)
                    return (cell)
                board.set(cell, ' ')

            # Choose the center if it's available
        if board.isempty(4):
            board.set(cell, self.sign)
            return 'B2'

            # Choose a corner if it's available
        for cell in ['A1', 'A3', 'C1', 'C3']:
            if board.isempty(cell):
                board.set(cell, self.sign)
                return (cell)

            # Choose any remaining space
        for cell in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
            if board.isempty(cell):
                board.set(cell, self.sign)
                return (cell)
