
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
    
    elif code ==10: 
        return ("1Robert: Yeah! Frank Lampard" + val + ".\n")

    

    
   
