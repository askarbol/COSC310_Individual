from Interface import reponse as res

## Here we check what the input from the user was and then determine which case
## we should activate for the response. Opcodes are checked before general string
## matching in order to handle specific cases.

name = None
favoriteFood = None

def interpolate(opcode, phrase):
    global name
    global favoriteFood

    if int(opcode) == 2:
        name = phrase
        return(res.formulateResponse(2, phrase))

    elif int(opcode) == 0:
        return(res.formulateResponse(1, ""))

    elif int(opcode) == 3:
        favoriteFood = phrase
        return(res.formulateResponse(31, phrase))

    else:    
        if "What's my name" in phrase:
            return(res.formulateResponse(3,name))
        
        elif "Thank" in phrase:
            return(res.formulateResponse(4,name))
        
        elif "How are you" in phrase:
            return(res.formulateResponse(33,""))

        elif "What is your favorite food" in phrase:
            return(res.formulateResponse(5,""))
        
        elif "It's nice today" in phrase:
            return(res.formulateResponse(6,""))
        
        elif "Do you have any hobbies" in phrase:
            return(res.formulateResponse(7,""))
        
        elif "What is your favorite sport" in phrase: 
            return (res.formulateResponse(8,""))
        
        elif "team do you support" in phrase:
            return (res.formulateResponse(9,""))
        
        elif "your favorite player" in phrase: 
            return (res.formulateResponse(10,""))
        
        elif "Are you married" in phrase: 
            return(res.formulateResponse(11,""))

        elif "Are you single" in phrase: 
            return(res.formulateResponse(11,""))
                   
        elif "Do you like to cook?" in phrase: 
            return (res.formulateResponse(12, favoriteFood))
        
        elif "How old are you" in phrase: 
            return (res.formulateResponse (13,""))
        
        elif "How tall are you" in phrase: 
            return (res.formulateResponse(14,""))
        
        elif "countries have you visited?" in phrase: 
            return (res.formulateResponse (15,""))
        
        elif "Where are you from" in phrase: 
            return (res.formulateResponse (16,"")) 
        
        elif "What is your name" in phrase: 
            return (res.formulateResponse (17,""))
        
        elif "I love you, Robert" in phrase: 
            return (res.formulateResponse (18,name))
        
        elif "What's your phone number" in phrase: 
            return (res.formulateResponse (19,"")) 
        
        elif "What languages do you speak" in phrase: 
            return (res.formulateResponse (20,"")) 
        
        elif "What is your goal in life" in phrase: 
            return (res.formulateResponse (21, name)) 
        
        elif "time of day do you feel best" in phrase: 
            return (res.formulateResponse (22,"")) 
        
        elif "sunrise or sunset" in phrase: 
            return (res.formulateResponse (23,"")) 
        
        elif "I wish I could watch one with you" in phrase: 
            return (res.formulateResponse (24,"")) 
        
        elif "Would you like to be famous" in phrase: 
            return (res.formulateResponse (25,"")) 
        
        elif "what's your github?" in phrase: 
            return (res.formulateResponse (26,"")) 
        
        elif "What kind of people do you like" in phrase: 
            return (res.formulateResponse (27,"")) 
        
        elif "last book you read" in phrase: 
            return (res.formulateResponse (28, name)) 
        
        elif "What do you do on the weekend" in phrase: 
            return (res.formulateResponse (29, name)) 
        
        elif "Goodbye Robert" in phrase: 
            return (res.formulateResponse (30, name))
            
        elif "Can I ask you some personal questions" in phrase: 
            return (res.formulateResponse (32,"")) 

        else :
            return(res.formulateResponse(0,""))
