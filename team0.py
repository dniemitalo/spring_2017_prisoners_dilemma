import random
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'EngageFizzyMode'
strategy_name = 'Top 3'
strategy_description = "Wingin' it"
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    while len(my_history)<10:
        if len(my_history)==0:
            return 'c'
        elif len(my_history)==1:
            return 'c'
        elif len(my_history)==2:
            return 'b'
        elif len(my_history)==3:
            return 'c'
        elif len(my_history)==4:
            return 'b'
        elif len(my_history)==5:
            return 'b'
        elif len(my_history)==6:
            return 'c'
        elif len(my_history)==7:
            return 'b'
        elif len(my_history)==8:
            return 'c'
        elif len(my_history)==9:
            return 'b'
    while len(my_history)>9:
        c = their_history.count('b')
        t = float(c)/len(their_history)
        n = my_history[-1]
        m = their_history[-1]
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
        if (their_history[-5:] == 'cbcbc') or (their_history[-5:] == 'bcbcb'):
            return 'b'
        elif (their_history[-5:] == 'bbbbb'):
            return 'b'
        elif (their_history[-5:] == 'ccccc'):
            return 'c'
        elif (their_history[-5:].count('b'))>2:
            return 'b'
        
        elif random.random()<.5:
            for round in range(len(my_history)-1):
                prior_round_them = their_history[round]
                prior_round_me = my_history[round]
                if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                    return their_history[round]
        elif random.random()<t:
            return 'b'
        elif n == 'b' and m == 'c':
            if random.random()<.65:
                return 'c'
        elif n == 'c' and m == 'c':
            if random.random()<.70:
                return 'c'
        elif (n == 'b' and m == 'b') or (n == 'c' and m == 'b'):
            if random.random()<.60:
                return 'b'
        else:
            return 'c'
        #else:
        #    return 'c'