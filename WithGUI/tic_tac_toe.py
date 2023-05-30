from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tic-Tac-Toe')

gameSize = Label(root, text="Enter square count you want in a row:")
gameSize.grid(column=0, row=2)
gameDimension = Entry(root, width=10)
gameDimension.grid(column=1, row=2)

player1 = Label(root, text="Enter first player's name(X)")
player1.grid(column=0, row=0)
player1Name = Entry(root, width=10)
player1Name.grid(column=1, row=0)
playerOneScore = 0  # gets updated when player1 wins
player1Score = Label(root, text="Player one score:"+str(playerOneScore))
player1Score.grid(row=4, column=0)

player2 = Label(root, text="Enter second player's name(O)")
player2.grid(column=0, row=1)
player2Name = Entry(root, width=10)
player2Name.grid(column=1, row=1)
playerTwoScore = 0  # gets updated when player2 wins
player2Score = Label(root, text="Player two score:"+str(playerTwoScore))
player2Score.grid(row=5, column=0)

startGame = Button(root, text="Start Game", height=2,
                   width=8, command=lambda: start())
startGame.grid(column=1, row=3)


# Start Game
def start():
    global clicked, buttonArr, totalBoxFilled
    clicked = True
    buttonArr = []  # will store each button in nxn matrix
    totalBoxFilled = 0  # used for draw check
    if (not gameDimension.get().isnumeric() or
            int(gameDimension.get()) < 2 or int(gameDimension.get()) > 9):
        messagebox.showerror("Tic Tac Toe", """Please enter size \n
                              between 2 and 9""")
        return
    for i in range(int(gameDimension.get())):
        buttonArr.append([])  # adding empty row to buttonArr
    for i in range(int(gameDimension.get())):
        for j in range(int(gameDimension.get())):
            button = Button(root, text=" ", height=4, width=8)
            buttonArr[i].append(button)
            buttonArr[i][j].grid(row=i+5, column=j+5)
            button["command"] = lambda button=button: buttonClick(button)
    # disabling players to change their names in-between the games
    player1Name.config(state=DISABLED)
    player2Name.config(state=DISABLED)
    gameDimension.config(state=DISABLED)
    player1Score["text"] = player1Name.get()+"'s score:"+str(playerOneScore)
    player1Score.grid(row=4, column=0)
    player2Score["text"] = player2Name.get()+"'s score:"+str(playerTwoScore)
    player2Score.grid(row=5, column=0)


# On button click
def buttonClick(button):
    global clicked, totalBoxFilled
    totalBoxFilled += 1

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        checkifwon()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", """Oops! 
            \nBox has already been selected \nPlease choose another box""")


# Function to check if a player won
def checkifwon():
    global playerOneScore, playerTwoScore

    # check if a player wins
    if (rowCheck() or columnCheck() or diagonal1Check() or diagonal2Check()):
        if(clicked == False):
            playerOneScore += 100
            messagebox.showinfo(
                "Tic Tac Toe", "CONGRATULATIONS! "+player1Name.get() + " Wins!!")
            player1Score["text"] = player1Name.get()+"'s score:" + \
                str(playerOneScore)
        else:
            playerTwoScore += 100
            messagebox.showinfo(
                "Tic Tac Toe", "CONGRATULATIONS! "+player2Name.get() + " Wins!!")
            player2Score["text"] = player2Name.get()+"'s score:" + \
                str(playerTwoScore)
        disableAllButtons()
    # check if game is draw
    elif (totalBoxFilled == int(gameDimension.get())**2):
        messagebox.showinfo(
            "Tic Tac Toe", "GAME DRAW ")
        disableAllButtons()


# Check for row win
def rowCheck():
    for i in range(int(gameDimension.get())):
        count = 0
        while(count < int(gameDimension.get()) and
              (buttonArr[i][0]['text'] == "X" or
               buttonArr[i][0]['text'] == "O") and
                buttonArr[i][0]['text'] == buttonArr[i][count]['text']):
            count += 1
            continue
        if count == int(gameDimension.get()):
            return True
    return False


# Check for column win
def columnCheck():
    for j in range(int(gameDimension.get())):
        count = 0
        while(count < int(gameDimension.get()) and
              (buttonArr[0][j]['text'] == "X" or
               buttonArr[0][j]['text'] == "O") and
                buttonArr[0][j]['text'] == buttonArr[count][j]['text']):
            count += 1
            continue
        if count == int(gameDimension.get()):
            return True
    return False


# Check for diagonal1(\) win
def diagonal1Check():
    count = 0
    while(count < int(gameDimension.get()) and
          (buttonArr[0][0]['text'] == "X" or
            buttonArr[0][0]['text'] == "O") and
            buttonArr[0][0]['text'] == buttonArr[count][count]['text']):
        count += 1
        continue
    if count == int(gameDimension.get()):
        return True
    return False


# Check for diagonal2(/) win
def diagonal2Check():
    count = 0
    while(count < int(gameDimension.get()) and
            (buttonArr[0][int(gameDimension.get())-1]['text'] == "X" or
             buttonArr[0][int(gameDimension.get())-1]['text'] == "O") and
            buttonArr[0][int(gameDimension.get())-1]['text'] == buttonArr[count][int(gameDimension.get())-1-count]['text']):
        count += 1
        continue
    if count == int(gameDimension.get()):
        return True
    return False


# Disable the buttons when game ends
def disableAllButtons():
    for i in range(0, int(gameDimension.get())):
        for j in range(0, int(gameDimension.get())):
            buttonArr[i][j].config(state=DISABLED)


# DriverCode
root.mainloop()
