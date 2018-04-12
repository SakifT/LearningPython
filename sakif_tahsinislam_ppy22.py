# Tahsin Islam Sakif
# 3rd April 2018
# CS293B
# Participation Project 21

vowel = ["a","e","i","o","u"]
stopProgram = False

while stopProgram==False:
    validInput=False
    while validInput==False:
        userInput1=(input("Enter a word to convert. Type stop to... stop."))
        userInput=userInput1.lower()
        if userInput.isalpha()==True:
            validInput=True
            stopProgram=True
            break
        if userInput.lower()=="stop":
            validInput=True
            stopProgram=True
            break
            
        else:
            print("The input is not only letters")



    emptyString=""
    if userInput[0] not in vowel:
        if userInput[1] not in vowel:
            pigString=userInput[2:]+userInput[0:2]+"ay"
        else:
            pigString=userInput[1:]+userInput[0]+"ay"
    else:
        pigString=userInput[1:]+userInput[0]+"yay"

    oddString=""
    tracker=0
    for key in pigString:
        if tracker%2==1:
            oddString=oddString+key
        tracker+=1
            
            
        

    print("Original PigLatin: ",pigString)
    print("Uppercase PigLatin: ",pigString.upper())
    print("Odd PigLatin: ",oddString)
        
