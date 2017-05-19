import random

team_name = 'Nemo'
strategy_name = 'Benevolent Tit for Tat'
strategy_description = 'Tit for Tat, but forgives sometimes.'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history)==0:
        return 'c'
    elif their_history[-1]=='b':
        if random.random()>0.09:
            return 'b'            
    return 'c'