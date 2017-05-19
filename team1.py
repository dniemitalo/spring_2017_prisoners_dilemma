team_name = 'TNG'
strategy_name = 'The Naughty Gooses'
strategy_description = '''
Try and counter their moves for the win.
'''

def move(my_history, their_history, my_score, their_score):
        if len(my_history)==0:
            return 'b'
        elif len(my_history)==1:
            return 'b'
        elif len(my_history)==2:
            return 'b'
        elif len(my_history)==3:
            return 'b'
        elif len(my_history)==4:
            return 'b'
        else:
            return 'b'
        if len(my_history)>=5: 
            if their_history[-5:]=='cbcbc' or their_history[-5:]=='bcbcb':
                return 'b'
            elif their_history[-5:]=='bbbbb':
                return 'b'
            elif their_history[-5:]=='ccccc':
                return 'c'
            else:
                return 'c' 


        
            
    
