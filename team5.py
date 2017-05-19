####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'TrumpTrain'
strategy_name = 'It is a secret.'
strategy_description = 'You will have to guess.'
letters = [ 'b', 'c',]
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history)==0:
        return 'c'
    elif len(their_history)>0 and len(their_history)<100 and their_history[-1]=='c':
        return(random.choice(letters))
    elif len(their_history)>100 and their_history[-1]=='b':
        return(random.choice(letters))
    else:
        return 'b'

