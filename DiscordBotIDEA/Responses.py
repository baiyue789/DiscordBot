import random

def messsrespond(message) -> str:
    offensive_words = ["fuck", "shit", "bitch", "asshole", "dick", "pussy", "cunt", "bastard",
                       "motherfucker", "nigger", "retard", "faggot", "whore", "slut", 'cock','fucker', 
                       'kill', 'motherfucker', 'motherfucke', 'ass', 'asshole']

    y = message.lower().split()
    user_message = message.lower()
    
    if user_message == 'why':
        return 'I know where you live'
    
    if any(word in offensive_words for word in y):
        return "bad message"
    if message != 0:
        x = random.randint(1,9)
        if x ==  1:
            return 'no'
        else:
            pass
        
    
    