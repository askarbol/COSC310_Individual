from tkinter import *
  
root = Tk() 
root.geometry("300x500") 
root.resizable(width=False, height=False)
root.title(" Q&A ") 
  
def Take_input(): 
    INPUT = inputtxt.get("1.0", "end-1c") 
    if (INPUT == ""): Output.insert(END, "PLEASE INPUT A SENTENCE.\n")
    else: Output.insert(END, "User: " + INPUT + "\n")
    

l = Label(text = "TEST APPLICAITON")

Output = Text(root, height = 18,  
              width = 30,  
              bg = "white") 

inputtxt = Text(root, height = 2, 
                width = 30, 
                bg = "white") 
  
Display = Button(root, height = 2, 
                 width = 10,  
                 text ="Send", 
                 command = lambda:Take_input()) 
  
l.pack(expand=TRUE)  
Output.pack(expand=TRUE) 
inputtxt.pack(expand=TRUE)
Display.pack(expand=TRUE) 
  
mainloop() 