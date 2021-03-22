from Interface import reponse as res
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()

## Here we check what the input from the user was and then determine which case
## we should activate for the response. Opcodes are checked before general string
## matching in order to handle specific cases.

name = None
favoriteFood = None

def psStem(e):
    words = e.split()
    stemmed = ""

    for w in words:
       stemmed += (ps.stem(w))
       stemmed += " "

    ## We take the input string, explode it into an array,
    ## stem each word, and recombine the stemmed sentence.
    return stemmed

def getPOS(e):
    words = e.split()
    sent = nltk.pos_tag(words)
    ## This will take the input phrase and return the part
    ## of speech code for the first word (NN: Singular Noun, NNS: Plural Noun etc.)
    ## list of codes can be found at https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
    return sent[0][1]


## To increase modularity of the system, we have the input recogniton
## in it's own file to make it easier to work on a specific part of
## the program, without having to search.
def interpolate(opcode, e):
    global name
    global favoriteFood

    phrase = psStem(e)

    ## First, check the opcodes to handle special conditions (i.e name input and first message)
    if int(opcode) == 2:
        if ((getPOS(e) == 'NN') or (getPOS(e) == 'NNS') or (getPOS(e) == 'NNP')):
            name = e
            return(res.formulateResponse(2, name))
        else:
            return(res.formulateResponse(34, e))


    elif int(opcode) == 0:
        ## The first message sent will always return the welcome string.
        return(res.formulateResponse(1, ""))


    elif int(opcode) == 3:
        if ((getPOS(e) == 'NN') or (getPOS(e) == 'NNS') or (getPOS(e) == 'NNP')):
            favoriteFood = e
            return(res.formulateResponse(31, favoriteFood))
        else:
            return(res.formulateResponse(35, e))

    ## If we've exhausted the possible opcodes, just check for string matching.
    else:    
        if psStem("What's my name") in phrase:
            return(res.formulateResponse(3,name))
        
        elif psStem("Thank") in phrase:
            return(res.formulateResponse(4,name))
        
        elif psStem("How are you") in phrase:
            return(res.formulateResponse(33,""))

        elif psStem("What is your favorite food") in phrase:
            return(res.formulateResponse(5,""))
        
        elif psStem("It's nice today") in phrase:
            return(res.formulateResponse(6,""))
        
        elif psStem("Do you have any hobbies") in phrase:
            return(res.formulateResponse(7,""))
        
        elif psStem("What is your favorite sport") in phrase: 
            return (res.formulateResponse(8,""))
        
        elif psStem("team do you support") in phrase:
            return (res.formulateResponse(9,""))
        
        elif psStem("your favorite player") in phrase: 
            return (res.formulateResponse(10,""))
        
        elif psStem("Are you married") in phrase: 
            return(res.formulateResponse(11,""))

        elif psStem("Are you single") in phrase: 
            return(res.formulateResponse(11,""))
                   
        elif psStem("Do you like to cook?") in phrase: 
            return (res.formulateResponse(12, favoriteFood))
        
        elif psStem("How old are you") in phrase: 
            return (res.formulateResponse (13,""))
        
        elif psStem("How tall are you") in phrase: 
            return (res.formulateResponse(14,""))
        
        elif psStem("countries have you visited?") in phrase: 
            return (res.formulateResponse (15,""))
        
        elif psStem("Where are you from") in phrase: 
            return (res.formulateResponse (16,"")) 
        
        elif psStem("What is your name") in phrase: 
            return (res.formulateResponse (17,""))
        
        elif psStem("I love you, Robert") in phrase: 
            return (res.formulateResponse (18,name))
        
        elif psStem("What's your phone number") in phrase: 
            return (res.formulateResponse (19,"")) 
        
        elif psStem("What languages do you speak") in phrase: 
            return (res.formulateResponse (20,"")) 
        
        elif psStem("What is your goal in life") in phrase: 
            return (res.formulateResponse (21, name)) 
        
        elif psStem("time of day do you feel best") in phrase: 
            return (res.formulateResponse (22,"")) 
        
        elif psStem("sunrise or sunset") in phrase: 
            return (res.formulateResponse (23,"")) 
        
        elif psStem("I wish I could watch one with you") in phrase: 
            return (res.formulateResponse (24,"")) 
        
        elif psStem("Would you like to be famous") in phrase: 
            return (res.formulateResponse (25,"")) 
        
        elif psStem("what's your github?") in phrase: 
            return (res.formulateResponse (26,"")) 
        
        elif psStem("What kind of people do you like") in phrase: 
            return (res.formulateResponse (27,"")) 
        
        elif psStem("last book you read") in phrase: 
            return (res.formulateResponse (28, name)) 
        
        elif psStem("What do you do on the weekend") in phrase: 
            return (res.formulateResponse (29, name)) 
        
        elif psStem("Goodbye Robert") in phrase: 
            return (res.formulateResponse (30, name))
            
        elif psStem("Can I ask you some personal questions") in phrase: 
            return (res.formulateResponse (32,"")) 

        ## If we couldn't find a match in the input, return "I don't understand."
        else :
            return(res.formulateResponse(0,""))
