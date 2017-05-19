team_name = 'NuclearFlamigos'
strategy_name = 'Deduction'
strategy_description = 'Collude unless opponents betrayal is less than 10 percent or more than 60 percent'
    
def move(my_history, their_history, my_score, their_score):
    opponent_moves = their_history.count ('b')
    
    if len(their_history) == 0:
        return 'c'
        
    elif float(len(their_history))/opponent_moves > .6:
        return 'b'
        
    elif float(len(their_history))/opponent_moves < .1:
        return 'b'
        
    else:
        return 'c'