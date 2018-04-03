"""
Tahsin Islam Sakif
13 February 2018
Homework Number 2
"""
WVtaxgrowthrate=0.01
WVApp=4700000000
WVBudget=4200000000
yearsbudget=0
newbudget=0
WVsixtaxgrowth=0.06
years4sixtax=0
twenty17budget=4200000000

while WVBudget<=WVApp:
    newbudget=WVBudget*(WVtaxgrowthrate+1)**yearsbudget
    if newbudget<WVApp:
        yearsbudget+=1
    else:
        break
print("Years it will take to overcome the deficit with 1% increase is: ",yearsbudget)
    

while twenty17budget<=WVApp:
    newbudget=WVBudget*(WVsixtaxgrowth+1)**years4sixtax
    if newbudget<WVApp:
        years4sixtax+=1
    else:
        break
print("Years it will take to overcome the deficit with 6% increase is: ",years4sixtax)

currentincome=float(input("What is your current income? "))
income=0
if currentincome<10000:
    income=currentincome*0.03
    print("Your income tax due is",income)
elif currentincome>=10000 and currentincome<25000:
    income=currentincome*0.04
    print("Your income tax due is",income)
elif currentincome>=25000 and currentincome<40000:
    income=currentincome*0.045
    print("Your income tax due is",income)
elif currentincome>=40000 and currentincome<60000:
    income=currentincome*0.06
    print("Your income tax due is",income)
elif currentincome>60000:
    income=currentincome*0.065
    print("Your income tax due is",income)
else:
    print("Invalid input.")

"""
I doubt that raising taxes on goods and services will cause that amount of
tax growth. The historic average of GDP growth rate is about half of 6 percent.
Raising taxes will just cause inequality between the rich and the poor. It
will hurt many small businesses and the wealthy will just move from West
Virginia to perhaps another counry to exploit tax advantages, lowering
the overall economy. I am no expert in US tax policies but these are my thoughts
on the matter. 
"""

    
        
        
