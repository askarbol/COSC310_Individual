from Interface import reponse as res

## Here we check what the input from the user was and then determine which case
## we should activate for the response. Opcodes are checked before general string
## matching in order to handle specific cases.

name = None

def interpolate(opcode, phrase):
    global name

    if int(opcode) == 2:
        name = phrase
        return(res.formulateResponse(2, phrase))

    elif int(opcode) == 0:
        return(res.formulateResponse(1, ""))

    else:    
        if "What's my name" in phrase:
            return(res.formulateResponse(3,name))
        
        if "Thank" in phrase:
            return(res.formulateResponse(4,name))
        
        if "What is your favourite food" in phrase:
            return(res.fomulateResponse(5,name))
        
        if "It is nice weather today" in phrase:
            return(res.fomulateResponse(6,name))
        
        if "Do you have any hobbies?" in phrase:
            return(res.fomulateResponse(7,name))
        
        if "Which is your favourite sport?" in phrase: 
            return (res.formulateResponse(8,name))
        
        if "Which team or club do you support?" in phrase:
            return (res.formulateResponse(9,name))
        
        if "Is there any player that you’re a fan of?" in phrase: 
            return (res.formulateResponse(10,name))
        
        if "Are you married or single?" in phrase: 
            return(res.formulateResponse(11,name))
                   
        if "Do you like to cook?" in phrase: 
            return (res.formulateResponse(12,name))
        
        if "How old are you?" in phrase: 
            return (res.formulateResponse (13, name))
        
        if "What's your height?" in phrase: 
            return (res.formulateResponse(14, name))
        
        if "Which countries have you visited?" in phrase: 
            return (res.formulateResponse (15, name ))
        
        if "Which country are you from" in phrase: 
            return (res.formulateResponse (16, name)) 
        
         if "What is your name?" in phrase: 
            return (res.formulateResponse (17,name))
        
        if "I love you, Robert" in phrase: 
            return (res.formulateResponse (18,name))
        
        if "What's your phone number?" in phrase: 
            return (res.formulateResponse (19, name)) 
        
        if "When did you learn English?" in phrase: 
            return (res.formulateResponse (20, name)) 
        


                    
                 

        else :
            return(res.formulateResponse(0,""))
