# a3.py
# Author - Shresth Kapila
# CMPT310 Assignment 3  
# ...

import random
import copy

# first = False

class tictactoe:
    # --representation/moves in tictactoe (stored as an array)
    # 0 1 2
    # 3 4 5
    # 6 7 8
    def __init__(self):
        self.structure = ['-'] * 9            # let 0 be the initial state of game
        self.currentPlayer = 'h'              # h <- human
        self.flag = 1

    def getStructure(self):
        return self.structure

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def getFlag(self):
        return self.flag

    def nextPlayer(self):
        if (self.currentPlayer == 'h'):
            self.currentPlayer = 'c'           # c <- (turn of) computer
        elif (self.currentPlayer == 'c'):
            self.currentPlayer = 'h'
        return self.currentPlayer

    def setFlag(self, setFlag):
        if setFlag == True:
            return self.flag
        else:
            self.flag = 2
            return self.flag

    def displayGame(self):
        print("-------------GAME STRUCTURE------------------")
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
        # while self.structure[pos] != '-':
        #     pos = int(input("Move not available, try another value: "))
        self.structure[pos] = player
        return pos

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

    def temp_puzzle(self):
        temp_game = tictactoe()
        temp_game.structure = self.structure[:]
        temp_game.currentPlayer = self.currentPlayer
        temp_game.flag = self.flag
        return temp_game

    
class MonteCarloSearchTree():
    def __init__(self, game):
        self.game = game
        self.structure = self.game.getStructure()
        self.state = self.game.checkStatus()
        self.playouts = 5000

    def randomPlayOuts(self, move):
        temp_game = copy.deepcopy(self.game) #self.game.temp_puzzle()
        temp_game.makeMove(move, temp_game.currentPlayer)
        temp_game.nextPlayer()
        status = temp_game.checkStatus()
        while status == -1:
            legal_moves = temp_game.legalMoves()
            randomMove = random.randint(0,8)
            while randomMove not in legal_moves:
                randomMove = random.randint(0,8)
            temp_game.makeMove(randomMove, temp_game.currentPlayer)
            temp_game.nextPlayer()
            temp_game.state = temp_game.checkStatus()
            status = temp_game.checkStatus()
        if temp_game.getFlag == 1:
            if status == 1:
                return 2
            elif status == 2:
                return -5
            else:
                return 1
        else:
            if status == 1:
                return -5
            elif status == 2:
                return 2
            else:
                return 1

    def makeMove(self):
        # print(first)
        # if first == True:
        legal_moves = self.game.legalMoves()
        maxWins = {k: 0 for k in legal_moves}
        # print(maxWins)
        for i in legal_moves:
            for _ in range(5000):
                maxWins[i] = maxWins[i] + self.randomPlayOuts(i)
        # print(maxWins)
        maxW = legal_moves[0]
        count = maxWins[maxW]
        for m in maxWins:
            if count <= maxWins[m]:
                maxW = m 
                count = maxWins[m]
        self.game.makeMove(maxW, self.game.currentPlayer)
        # else:
        #     legal_moves = self.game.legalMoves()
        #     r = random.randint(0,8)
        #     while r not in legal_moves and r != 4:
        #         r = random.randint(0,8)
        #     self.game.makeMove(r, self.game.currentPlayer)

# Display game structure
def gamePosition():
    print("-------------------")
    print("|  0  |  1  |  2  |")
    print("-------------------")
    print("|  3  |  4  |  5  |")
    print("-------------------")
    print("|  6  |  7  |  8  |")
    print("-------------------\n")

# Running game
def play_a_new_game():
    gamecontinue = 'y'

    while gamecontinue.lower() == 'y':
        game = tictactoe()
        mcst = MonteCarloSearchTree(game)
        status = game.checkStatus()
        print("\nHere the game begins, GOOD LUCK!!!")
        start = input("\nWanna start first? (type y/n): ")
        if(start.lower() == 'y'):
            game.setFlag(False)
            # first = False
            print("\n-------Your Turn-------")
            print("\nHere are the number on the tile of the game")
            gamePosition()
            game.displayGame()
            move = input("\nEnter the number of the tile to make your move: ")
        elif (start.lower() == 'n'):
            game.nextPlayer()
            mcst.makeMove()
            game.nextPlayer()
            print("\n****Computer will move......\n")
            game.displayGame()
            move = input("\nEnter the number of the tile to make your move: ")
        else:
            game.setFlag(False)
            print("\n-------Your Turn-------")
            print("\nLooks like you are confused, I will let you start first!!")
            print("\nHere are the number on the tile of the game")
            gamePosition()
            game.displayGame()
            move = input("\nEnter the number of the tile to make your move: ")
        while (status == -1):
            move = game.makeMove(move, game.getCurrentPlayer())
            print("\nHere are the number on the tile of the game")
            gamePosition()
            game.displayGame()
            # print(game.getCurrentPlayer())
            game.nextPlayer()
            mcst.makeMove()
            # first = True
            status = game.checkStatus()
            print("\n****Computer will move......\n")
            game.displayGame()
            # print(status)
            if (status == -1):
                game.nextPlayer()
                print("\n-------Your Turn-------")
                print("\nHere are the number on the tile of the game")
                gamePosition()
                game.displayGame()
                move = input("\nEnter the number of the tile to make your move: ")
                temp_game = game.temp_puzzle()
                move = game.makeMove(move, temp_game.getCurrentPlayer())
                print("\nHere are the number on the tile of the game")
                gamePosition()
                game.displayGame()
                status = game.checkStatus()
                # print(status)
        game.makeMove(move, game.getCurrentPlayer())
        print("\nGame End!!")
        game.displayGame()
        if status == 1:
            print("\nCongratulations: You WON\n")
        elif status == 2:
            print("\nYou lost, try again\n")
        else:
            print("\nDRAW: No one wins\n")
        gamecontinue = input("Type 'y' to try again or press any key to terminate: \n")


if __name__ == '__main__':
  play_a_new_game()

