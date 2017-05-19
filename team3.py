team_name = 'Unikitty' # Only 10 chars displayed.
strategy_name = 'not mad just dissapointed'
strategy_description = 'colludes until betrayed then retaliates with betray for 3 rounds then goes back to colluding'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif 'b' in their_history[-3:]:
        return 'b'
    else:
        return 'c'