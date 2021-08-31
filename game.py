import random


def printLine():
    return print("------------------------")

print(
        "************************************************"
        "\nWelcome To ROCK PAPER SCISSOR"                                  
        "\nEnter rock, paper or scissor"  
       '\nif rock    v/s  scissor    rock wins'
        '\nif rock    v/s  paper      paper wins'
        '\nif scissor v/s  paper      scissor wins' 
        '\nMay Fortune favours you' 
        "\nEnter 'quit' to end the game."      
        "\n*************************************************"                             
                                        )
userRound = ''
elements = ['rock', 'paper', 'scissor']
complement = {'rock':'scissor', 'scissor':'paper', 'paper':'rock', 'quit':'quit'}



def play(userRound):
    pcRound = random.choice(elements)
    try:
        if pcRound.lower() == complement[userRound.lower()]:
            print(">> "+pcRound.lower())
            print("You won")
            
        elif userRound.lower() == complement[pcRound.lower()]:
            print(">> "+pcRound.lower())
            print("You loose")

        elif userRound.lower() == pcRound.lower():
            print(">> "+pcRound.lower())
            print("It's a tie.")
   
    except KeyError:
        print("Check your spelling!!")
    
    printLine()
    


while userRound.lower() != 'quit':
    userRound = input(">> ")
    play(userRound)
    