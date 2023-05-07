#Kept on getting an syntax error from the templet code


import random


# ASCII art Sourced from github user wynand1004


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def printMove(move):
	if move == 'rock':
		return rock
	if move == 'paper':
		return paper
	if move == 'scissors':
		return scissors


def makeComputerMove(computerName):
        #Will produce a random number 0 - 2 to choose what it plays
        computerMove = random.randint(0,2)
        #if statement to print out the move that it is making
        if computerMove == 0:
                computerMove = "rock"
                print(computerName + " chose: ")
                print(printMove(computerMove))
        elif computerMove == 1:
                computerMove = "paper"
                print(computerName, " chose: ")
                print(printMove(computerMove))
        elif computerMove == 2:
                computerMove = "scissors"
                print(computerName + " chose: ")
                print(printMove(computerMove))
        return computerMove


def makePlayerMove(playerName):
        #input for the player so that it can make a move
        print("")
        playerMove = input("Do you want to use rock, paper, or scissors? ")
        #make the input into lower case so that the computer can read it 
        playerMoveLower = playerMove.lower()
        while playerMoveLower != "paper"  and playerMoveLower != "rock" and playerMoveLower != "scissors":
                print("")
                print("That is not a valid input.")
                print("")
                playerMove = input("Do you want to use rock, paper, or scissors? ")
                playerMoveLower = playerMove.lower()
        #just adds a space (I think it looks better)
        print("")
        print(playerName + " chose: ")
        print(printMove(playerMoveLower))
        
        return playerMoveLower


def checkRoundWinner(x, y, playerName, computerName):
        #to see if the inputs are equal to each other
        if x == y:
                print("It was a tie!")
        #will run throught the results 
        elif x == "rock":
                if y == "paper":
                        player = "Player Wins"
                        print(playerName + " won the round!")
                        return player
                else:
                        computer = "Computer Wins"
                        print(computerName + " won the round!")
                        return computer
        elif x == "paper":
                if y == "scissors":
                        player = "Player Wins"
                        print(playerName + " won the round!")
                        return player
                else:
                        computer = "Computer Wins"
                        print(computerName + " won the round!")
                        return computer
        elif x == "scissors":
                if y == "rock":
                        player = "Player Wins"
                        print(playerName + " won the round!")
                        return player
                else:
                        computer = "Computer Wins"
                        print(computerName + " won the round!")
                        return computer
def main():
        #Prompt to make a name
        playerName = str(input("What is your name? "))
        computerName = "R2D2"
        #sets the wins to 0 for each
        computerWins = 0
        playerWins = 0
        #to loop untill someone hits 2 wins
        while computerWins < 2 and playerWins < 2:
                playerMove = makePlayerMove(playerName)
                computerMove = makeComputerMove(computerName)
                win = checkRoundWinner(computerMove, playerMove, playerName, computerName)
                #checks for the winner
                if win == "Player Wins":
                        playerWins = playerWins + 1
                elif win == "Computer Wins":
                        computerWins = computerWins + 1
        #Returns the statement for who won
        if playerWins == 2:
                print("")
                print(playerName + " won the match!")
        else:
                print("")
                print(computerName + " won the match!")
                
                
main()
        
