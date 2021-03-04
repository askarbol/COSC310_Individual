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

    else:    
        if "Hello" in phrase:
            return(res.formulateResponse(1,""))

        elif "What's my name" in phrase:
            return(res.formulateResponse(3,name))
            
        else :
            return(res.formulateResponse(0,""))