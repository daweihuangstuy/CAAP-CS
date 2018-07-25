# YOUR NAME
# ASSIGNMENT

from random import randint
import math

# global variable of chutes and ladders
gameBoard = []
# remember to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
	return randint(1,6)

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
    for i in range(1, int(w)*int(l) + 1):
        global gameBoard
        gameBoard.append(i)

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
    if d == 4 or d == 8 or d == 12 or d == 14:
        return True
    else:
        return False

def printPositions(list1):
    tempStr = "\nThe positions of each player are:\n"
    for i in list1:
        tempStr += "Player " + i["player"] + ": " + str(i["position"]) + "\n"
    return tempStr
    
# function to make and play a game
def play_game(mode, players1):
    state = []
    if (mode == "pc"):
        playerDict = {"player" : "computer", "state" : mode, "moves" : 0, "position" : 1 }
        state.append(playerDict)
# start of game
        while state[0]["position"] < len(gameBoard):
            state[0]["position"] += roll_die()
            if is_chutes_ladders(state[0]["position"]):
                state[0]["position"] = chutes_ladders[state[0]["position"]]
            state[0]["moves"] += 1
        return state[0]["moves"]
    
    if (mode == "user"):
        playerDict = {"player" : "user", "state" : "user", "moves" : 0, "position" : 1 }
        state.append(playerDict)
        for i in range(1, int(players1)):
            playerDict1 = {"player" : "Computer" + str(i), "state" : "pc", "moves" : 0, "position" : 1 }
            state.append(playerDict1)
# start of game
        stop = True
        n = 0
        while stop:
            while stop:
                diceRoll = roll_die()
                if state[n % len(state)]["player"] == "user":
                    print (printPositions(state))
                    if input("Type ok to roll dice: ") == "ok":
                        print("You rolled a " + str(diceRoll))                    
                state[n % len(state)]["position"] += diceRoll
                if is_chutes_ladders(state[n % len(state)]["position"]):
                    state[n % len(state)]["position"] = chutes_ladders[state[n % len(state)]["position"]]
                state[n % len(state)]["moves"] += 1
                if state[n % len(state)]["position"] >= len(gameBoard):
                    stop = False
                    print(state[n % len(state)]["player"].upper() + " WON THE GAME!!!")
                    break
                n += 1
                    
# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game():
    modeType = input("What is the mode of your game? 'pc' or 'user'?: ")
    length = input("What is the length of your gameboard?: ")
    width = input("What is the width of your gameboard?: ")
    makeGame(width, length)
    if (modeType == "pc"):
        gameNumber = input("How many times do you want to play this game?: ")
        moveCounter = 0
        for i in range(0, int(gameNumber)):
            moveCounter += play_game(modeType, 1)
        print("\nEach game has on average: " + str(float(moveCounter)/float(gameNumber)) + " moves!")
    if (modeType == "user"):
        playerNum = input("How much players (including yourself) do you want in your game?: ")
        play_game(modeType, playerNum)
    
simulate_game()
    