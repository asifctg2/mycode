#!/usr/bin/env python3  
#show question 
#ask input for the answer
#capitalize the answer
#check the answer
#statement for correct
#statement for incorrect
quiz = {"What is the capital of Spain? ":"Madrid",
         "What is the capital of Turkey? ": "Ankara",
         "What is the capital of Chile? ": "Rancagua"
         }

counter = 0

for question in quiz:
    while counter < 3:
        counter +=1
        name = input("enter your name:")
        print("hello", name,"welcome to quiz about capital city")
        #---------------
        answer = input(question + ":")
        if answer==quiz[question]
       
        #---------------

        break



