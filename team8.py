team_name = 'NuclearFlamigos'
strategy_name = 'Deduction'
strategy_description = 'Collude unless opponents betrayal is less than 10 percent or more than 60 percent'
def percentage(part, whole):
    x = 100 * float(part)/float(whole)
    return x
        
def move(my_history, their_history, my_score, their_score):
    opponent_moves = their_history.count ('b') + 1
    history =  len(their_history) + 1
    
    if len(their_history) == 0:
            return 'c'
            
    elif percentage(history, opponent_moves) > 60:
            return 'b'
            
    elif percentage(history, opponent_moves) < 10:
            return 'b'
            
    else:
            return 'c'