"""
Created on Thu Jan 18 09:21:30 2024

@author: cmj17
"""

"""PsuedoCode for Knock Knock
print "What is your name?"
get name by inserting an input in that question

Print "Hey [name], do you want to hear a joke? [Y/N]"
require an input to the question

create if statement that detects whether the answer was a "Yes" or "No"
    if the answer starts with a "y", then move onto the joke and print "Knock Knock"
    else, have the computer state "It was going to be really funny" and end program

create if statement for an answer to "Knock Knock"
    if answer is "Who's there?", output "Atch"
    else, "you were supposed to say 'atch who?' " and end program
    
create if statement that states 
    if input is "atch who?", print "bless you"
"""
print("What is your name?")
name=input()
print("Hello, " + name +" would you like to hear a joke?")
yn=input()

if yn=="yes"or"Yes":
    print("Knock Knock")
    who=input()
else:
    print("It was going to be funny")
    

if who=="who's there?"or"Who's there?" or "whos there?" or "Whos there?":
    print("Atch")
    atch=input()
else:
    print("You were supposed to say Who's there?")
if atch=="Atch who?" or "atch who?" or "atch who" or "Atch who":
    print("Don't cry, its just a joke!")
else:
    print("You were supposed to say Atch who?")
