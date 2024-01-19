# -*- coding: utf-8 -*-
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
    else, have the computer state "It was going to be really funny"

create if statement for an answer to "Knock Knock"
    if answer is "Who's there?", output "Atch"
    else, "you were supposed to say 'atch who?' "
    
create if statement that states 
    if input is "atch who?", print "bless you"
"""
print("What is your name?")
name=input()
print("Hello, " + name +" would you like to hear a joke?")
yn=input()

if yn=="yes":
    print("Knock Knock")
else:
    print("It was going to be funny")