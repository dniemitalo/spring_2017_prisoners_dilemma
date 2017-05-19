####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DANK V2' # Only 10 chars displayed.
strategy_name = 'you never know'
strategy_description = 'If other team says b we return b if the length is more than 8 we return b if the length is less than 3 we return b, if else we return c'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)<3:
        return 'b'
    elif len(my_history)>8:
        return 'b' 
    elif 'b' in their_history:
        return 'b'   
    else:
        return 'c'  
              