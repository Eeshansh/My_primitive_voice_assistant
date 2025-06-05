from Listen import MicExecution
import random

from Speak import Speak1




def game_play():
    Speak1("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<10):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = MicExecution().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                Speak1("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak1("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak1("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                Speak1("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                Speak1("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak1("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                Speak1("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak1("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak1("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    Speak1(f"FINAL SCORE: you scored :- {Me_score} points : I scored :- {Com_score} points")
    Speak1("Game Over!!")
    

            