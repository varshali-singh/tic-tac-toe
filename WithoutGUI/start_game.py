from player import Player
from tic_tac_toe import TicTacToe
from symbols import Symbol


#Initialization of game
class StartGame:
    def __init__(self):
        self.__player1 = self.__setPlayer(1)
        self.__player2 = self.__setPlayer(2)
        self.__dimension = self.__setDimension()

    def __setDimension(self):
        dimension = input(
            "Please enter board size between 3 to 8 in integer: ")
        while(not dimension.isnumeric() or int(dimension) > 8 or int(dimension) < 3):
            dimension = input("Please Enter Correct Dimension: ")
        return int(dimension)

    def __setPlayer(self, playerNumber):
        playerName = str(input("Please enter player" +
                         str(playerNumber) + " name: "))
        if(playerNumber == 1):
            playerSymbol = Symbol.X.value
        else:
            playerSymbol = Symbol.O.value
        return Player(playerName, playerSymbol)

    def playGame(self):
        game = TicTacToe(self.__dimension, self.__player1, self.__player2)
        game.play()
        playMore = input("Do you want to play another game[Yes/No]: ")
        while(not(playMore == "Yes" or playMore == "No")):
            playMore = input("Please input either Yes or No: ")
        if (playMore == "Yes"):
            self.playGame()
        elif (playMore == "No"):
            print("Final scores:")
            print(self.__player1.name, ": ", self.__player1.score)
            print(self.__player2.name, ": ", self.__player2.score)
            
