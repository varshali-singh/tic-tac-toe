class TicTacToe:
    def __init__(self, size, player1=None, player2=None):
        self.__dimension = size
        self.__player1 = player1
        self.__player2 = player2
        self.__currentChance = 0
        self.__playerWon = False
        self.__emptySpacesCount = size**2
        self.__board = [["" for i in range(self.__dimension)]
                      for j in range(self.__dimension)]
                      
    #displays board after every move
    def __showBoard(self):
        print("\n")
        for i in range(self.__dimension):
            for j in range(self.__dimension):
                print("\t", self.__board[i][j], end="  ")
            print("\n")

    #displays board for the first time
    def __initializeBoard(self):
        count = 1
        print("\tLet's play Tic-Tac-Toe!!!\n")
        print("\tChoose a cell numbered from 1 to",
              self.__dimension**2, "as below and play\n\n")
        for i in range(self.__dimension):
            for j in range(self.__dimension):
                self.__board[i][j] = count
                print("\t", self.__board[i][j], end="  ")
                count += 1
            print("\n")

    #check for row win
    def __rowCheck(self):
        for i in range(self.__dimension):
            count = 0
            while(count < self.__dimension and
                    self.__board[i][0] == self.__board[i][count]):
                count += 1
                continue
            if count == self.__dimension:
                self.__playerWon = True
                return True
        return False

    #check for column win
    def __columnCheck(self):
        for j in range(self.__dimension):
            count = 0
            while(count < self.__dimension and
                    self.__board[0][j] == self.__board[count][j]):
                count += 1
                continue
            if count == self.__dimension:
                self.__playerWon = True
                return True
        return False

    #check for diagonal1(\) win
    def __diagonal1Check(self):
        count = 0
        while(count < self.__dimension and
                self.__board[0][0] == self.__board[count][count]):
            count += 1
            continue
        if count == self.__dimension:
            self.__playerWon = True
            return True
        return False

    #check for diagonal2(/) win
    def __diagonal2Check(self):
        count = 0
        while(count < self.__dimension and
                self.__board[0][self.__dimension-1] == self.__board[count][self.__dimension-1-count]):
            count += 1
            continue
        if count == self.__dimension:
            self.__playerWon = True
            return True
        return False
    
    #checks valid input given by player
    def __checkValidInput(self, inputNum, symbol):
        rowNum = (inputNum-1)//self.__dimension
        colNum = (inputNum-1) % self.__dimension
        if (inputNum > 0 and inputNum <= self.__dimension**2 and
                type(self.__board[rowNum][colNum]) == int):
            self.__board[rowNum][colNum] = symbol
            return
        else:
            newInput = input("Please Enter Valid Number: ")
            while (not newInput.isnumeric()):
                newInput = input("Please Enter Valid Number: ")
            self.__checkValidInput(int(newInput), symbol)
    
    #game play execution
    def play(self):
        input1 = 0
        self.__initializeBoard()
        while (not self.__rowCheck() and
               not self.__columnCheck() and
               not self.__diagonal1Check() and
               not self.__diagonal2Check() and
               self.__emptySpacesCount != 0):
            if (self.__currentChance == 0):
                input1 = input(self.__player1.name +
                               "'s chance. Please choose your number: ")
                while(not input1.isnumeric()):
                    input1 = input(self.__player1.name +
                                   "'s chance. Please choose correct number: ")
                self.__checkValidInput(int(input1), self.__player1.symbol)
            else:
                input1 = input(self.__player2.name +
                               "'s chance please choose your number: ")
                while(not input1.isnumeric()):
                    input1 = input(self.__player2.name +
                                   "'s chance. Please choose correct number: ")
                self.__checkValidInput(int(input1), self.__player2.symbol)
            self.__currentChance = (self.__currentChance+1) % 2
            self.__emptySpacesCount -= 1
            self.__showBoard()
        if self.__emptySpacesCount == 0 and self.__playerWon == False:
            print("Game Draw!")
        elif self.__currentChance == 1:
            print(self.__player1.name, " won!")
            self.__player1.score += 100
        elif self.__currentChance == 0:
            print(self.__player2.name, " won!")
            self.__player2.score += 100
        return
