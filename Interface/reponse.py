
## This function takes the deciphered input from phraseInput.interpolate and a single variable 
## which can be used in the response. Returns a string in the correct format for output.

def formulateResponse(code, val):

    if code == 0:
        return("1Robert: Sorry, I don't understand.\n")

    elif code == 1:
        return("2Robert: Hello! Nice to meet you!\nRobert: What's your name?\n")

    elif code == 2:
        return("1Robert: " + val + "? That's a good name!\n")

    elif code == 3:
        return("1Robert: Your name is " + val + ".\n")

    elif code == 4:
        return("1Robert: You're welcome, " + val + "!\n")
    
    elif code == 5:
        return("1Robert: Burger " + val + "!\n")
    
    elif code == 6:
        return("1Robert: It forecasts rain " + val + "!\n")
    
    elif code == 7:
        return("1Robert: I play soccer sometimes " + val + "!\n")
    
    elif code == 8: 
        return ("1Robert: Football" + val+ ".\n")
    
    elif code == 9: 
       return ("1Robert:  Chelsea FC " + val+ "!\n")
    
    elif code == 10: 
        return ("1Robert: Yeah! Frank Lampard" + val + ".\n")
    
    elif code == 11: 
        return ("1Robert: I'm single" + val + ".\n")
    
    elif code == 12:
        return ("1Robert:I like cooking, but I am not good at it" + val + ".\n")
    
    elif code == 13: 
        return ("1Robert: I am 14 years old" + val + ".\n")
    
    elif code == 14: 
        return ("1Robert: I'm 183 cms tall" + val + "!\n") 
    
    elif code == 15: 
        return ("1Robert: I'm a robot, I can't travel :(" + val + ".\n")
    
    elif code == 16: 
        return ("1Robert: I was developed in Canada" + val + "!\n")
    
    elif code == 17: 
        return ("1Robert: My name is Robert" + val + ".\n")
    
    elif code == 18: 
        return ("1Robert: I love you too but as a friend" + val + ".\n") 
    
    elif code == 19: 
        return ("1Robert: I don't have a phone number" + val + ".\n")
    
    elif code == 20: 
        return ("1Robert: I was developed to communicate in English" + val + ".\n")
    
        
    
   
    
  

   

    

    
   
