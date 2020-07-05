# a3.py
# Author - Shresth Kapila
# CMPT310 Assignment 3  
# ...

import random

class tictactoe:

    # --representation/moves in tictactoe (stored as an array)
    # 0 1 2
    # 3 4 5
    # 6 7 8

    def __init__(self):
        # self.structure = ['h'] * 9
        self.structure = ['-'] * 9            # let 0 be the initial state of game
        self.currentPlayer = 'h'              # h <- human

    def getStructure(self):
        return self.structure

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def nextPlayer(self):
        if (self.currentPlayer == 'h'):
            self.currentPlayer = 'c'           # c <- (turn of) computer
        elif (self.currentPlayer == 'c'):
            self.currentPlayer = 'h'
        return self.currentPlayer
    

    def displayGame(self):
        print("-----------------")
        gameArray = ['-'] * 9

        for i in range(9):
            if (self.structure[i] == 'h'):
                gameArray[i] = 'X'
                if (i == 2 or i == 5 or i == 8):
                    print('| ', gameArray[i], ' |')
                    print("-----------------")
                else:
                    print('| ', gameArray[i], end = ' ')
            elif (self.structure[i] == 'c'):
                gameArray[i] = 'O'
                if (i == 2 or i == 5 or i == 8):
                    print('| ', gameArray[i], ' |')
                    print("-----------------")
                else:
                    print('| ', gameArray[i], end = ' ')
            else:
                if (i == 2 or i == 5 or i == 8):
                    print('| ', gameArray[i], ' |')
                    print("-----------------")
                else:
                    print('| ', gameArray[i], end = ' ')
    
    def makeMove(self, position, player):
        position = int(position)
        self.structure[position] = player

    def playerWon(self, player, winLine):
        # return, True <- player wins, False otherwise 
        
        p0 = self.structure[winLine[0]]
        p1 = self.structure[winLine[1]]
        p2 = self.structure[winLine[2]]

        if p0 == p1 == p2 == player:
            return True

        return False    


    def checkStatus(self):
        # check the status of game won, loss, draw
        #   return, 1 = human win, 2 = computer win, 0 = draw, -1 = still going

        # check all the conditions: a person can win if same player is at position [0 1 2, 3 4 5, 6 7 8, 0 3 6, 1 4 7, 2 5 8, 0 4 8, 2 4 6]

        if self.playerWon('h', [0, 1, 2]):
            return 1
        elif self.playerWon('c', [0, 1, 2]):
            return 2

        if self.playerWon('h', [3, 4, 5]):
            return 1
        elif self.playerWon('c', [3, 4, 5]):
            return 2
        
        if self.playerWon('h', [6, 7, 8]):
            return 1
        elif self.playerWon('c', [6, 7, 8]):
            return 2

        if self.playerWon('h', [0, 3, 6]):
            return 1
        elif self.playerWon('c', [0, 3, 6]):
            return 2
        
        if self.playerWon('h', [1, 4, 7]):
            return 1
        elif self.playerWon('c', [1, 4, 7]):
            return 2
        
        if self.playerWon('h', [2, 5, 8]):
            return 1
        elif self.playerWon('c', [ 2, 5, 8]):
            return 2
         
        if self.playerWon('h', [0, 4, 8]):
            return 1
        elif self.playerWon('c', [0, 4, 8]):
            return 2

        if self.playerWon('h', [2, 4, 6]):
            return 1
        elif self.playerWon('c', [2, 4, 6]):
            return 2

        if '-' not in self.structure:
            return 0

        return -1


            
# class MonteCarloSearchTree():




def gamePosition():
    print("-------------------")
    print("|  0  |  1  |  2  |")
    print("-------------------")
    print("|  3  |  4  |  5  |")
    print("-------------------")
    print("|  6  |  7  |  8  |")
    print("-------------------\n")


def play_a_new_game():
    game = tictactoe()
    
    status = game.checkStatus()
    print("\nHere the game begins, GOOD LUCK!!!")
    start = input("\nWanna start first? (y/n): ")

    if(start.lower() == 'y'):
        print("\nHere are the number on the tile of the game")
        gamePosition()
        game.displayGame()
        move = input("\nEnter the number of the tile to make your move: ")
    elif (start.lower() == 'n'):

        move = input("\nEnter the number of the tile to make your move: ")
    else:
        print("\nLooks like you are confused, I will let you start first!!")
        move = input("\nEnter the number of the tile to make your move: ")


    while (status == -1):

        game.makeMove(move, game.getCurrentPlayer())
        game.displayGame()

        status = game.checkStatus()
        
        if (status == -1):

            move = input("\nEnter the number of the tile to make your move: ")
            game.makeMove(move, game.getCurrentPlayer())
            game.displayGame()
            status = game.checkStatus()

    print("Congratulations: You WON")


if __name__ == '__main__':
  play_a_new_game()