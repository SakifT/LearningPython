"""
Tahsin Islam Sakif
February 13th 2018
CS 293B
Participation Project 11
"""


Feline=("Tiger", "Lion", "Cheetah")
Canine=("Dog", "Wolf", "Fox")
Reptile=("Snake", "Crocodile", "Iguana")
zoo=[Feline,Canine,Reptile]
userInput=""

while userInput != "stop":
    userInput=input("Enter an animal of your choice: ")
    animalFound=False
    for kingdom in zoo:
        if userInput in kingdom:
            animalFound=True
            print("That animal is in the Zoo.")
            break
        else:
            animalFound=False
            print("That animal is not in the Zoo.")
            break
        
            
