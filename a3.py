# a3.py
# Author - Shresth Kapila
# CMPT310 Assignment 3  
# ...

import random

flag = False

class tictactoe:

    # --representation/moves in tictactoe (stored as an array)
    # 0 1 2
    # 3 4 5
    # 6 7 8

    def __init__(self):
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
        pos = int(position)
        self.structure[pos] = player

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
    
    def legalMoves(self):
        moves = []
        for i in range(9):
            if self.structure[i] == '-':
                moves.append(i)
        return moves


            
class MonteCarloSearchTree():

    def __init__(self, game):
        self.game = game
        # self.playouts = 10000

    def randomPlayOuts(self, move, legal_moves):
        temp_game = tictactoe()
        temp_game.structure = self.game.structure[:]
        temp_game.currentPlayer = self.game.getCurrentPlayer()
        temp_game.makeMove(move, temp_game.currentPlayer)
        temp_game.nextPlayer()
        status = temp_game.checkStatus()

        while status == -1:
            randomMove = random.randint(0,8)

            while randomMove not in legal_moves:
                randomMove = random.randint(0,8)
            temp_game.makeMove(randomMove, temp_game.currentPlayer)
            temp_game.nextPlayer()
            status = temp_game.checkStatus()

        if flag == False:
            if status == 1:
                return 2
            elif status == 2:
                return -2
            else:
                return 1
        else:
            if status == 1:
                return -2
            elif status == 2:
                return 2
            else:
                return 1


    def makeMove(self):
        legal_moves = self.game.legalMoves()
        maxWins = {k: 0 for k in legal_moves}
        # print(maxWins)
        for i in legal_moves:
            for j in range(10000):
                maxWins[i] = maxWins[i] + self.randomPlayOuts(i, legal_moves)
        print(maxWins)
        maxW = legal_moves[0]
        count = maxWins[maxW]
        for k in maxWins:
            if count < maxWins[k]:
                maxW = k
                count = maxWins[k]
        self.game.makeMove(maxW, self.game.currentPlayer)

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
    mcst = MonteCarloSearchTree(game)
    
    status = game.checkStatus()
    print("\nHere the game begins, GOOD LUCK!!!")
    start = input("\nWanna start first? (y/n): ")

    if(start.lower() == 'y'):
        print("\nHere are the number on the tile of the game")
        gamePosition()
        game.displayGame()
        flag = True
        move = input("\nEnter the number of the tile to make your move: ")
    elif (start.lower() == 'n'):
        game.nextPlayer()
        mcst.makeMove()
        game.nextPlayer()
        game.displayGame()
        move = input("\nEnter the number of the tile to make your move: ")
    else:
        print("\nLooks like you are confused, I will let you start first!!")
        print("\nHere are the number on the tile of the game")
        gamePosition()
        game.displayGame()
        move = input("\nEnter the number of the tile to make your move: ")

    while (status == -1):
        game.makeMove(move, game.getCurrentPlayer())
        game.displayGame()

        # print(game.getCurrentPlayer())
        game.nextPlayer()
        # print(game.getCurrentPlayer())
        
        status = game.checkStatus()
        # print(status)
        mcst.makeMove()
        status = game.checkStatus()
        # print(status)
        if (status == -1):
            game.nextPlayer()
            game.displayGame()
            move = input("\nEnter the number of the tile to make your move: ")
            game.makeMove(move, game.getCurrentPlayer())
            game.displayGame()
            status = game.checkStatus()
            # print(status)
    game.makeMove(move, game.getCurrentPlayer())

    if status == 1:
        print("Congratulations: You WON")
    elif status == 2:
        print("You lost, trya again")
    else:
        print("DRAW: No one wins")


if __name__ == '__main__':
  play_a_new_game()