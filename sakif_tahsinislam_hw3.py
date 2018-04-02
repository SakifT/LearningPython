"""
Tahsin Islam Sakif
25 February 2018
CS 293B
Homework 3
"""

from statistics import *

Berkeley = [16,22,16,22,28,33,46,46,48]
McDowell = [18,23,23,24,26,15,22,22,28]
Mercer = [25,29,14,34,51,37,25,47,38]
Raleigh = [22,19,12,45,60,58,37,39,62]

def functionAverage(String,list1):
    average=mean(list1)

    return (String,average)

def functionZScore(zscoredata):
    zscoreNEW=[]
    for i in zscoredata:
        (i-mean(zscoredata)/stdev(zscoredata))
        zscoreNEW.append((i-mean(zscoredata))/stdev(zscoredata))
    return zscoreNEW

def functionYear(String,list2):
    print(functionAverage(String,list2))
    for year in range(0,9):
        print("In the year:",year+2007)
        print("The number of deaths is:",list2[year])
        print("The z score is:",functionZScore(list2)[year])

def main():
    functionYear("Berkeley",Berkeley)
    functionYear("McDowell",McDowell)
    functionYear("Mercer",Mercer)
    functionYear("Raleigh",Raleigh)

if __name__== "__main__":
    main()
    

"""
The drug overdoses have generally increased in all of the counties.
Some counties such as Raleigh are having more deaths than the other ones.
I propose that there should be more awareness to the locals there on
the dangers of drug overdose, and have a stricter law to prevent these deaths.
Best solution is to make the public more aware of its risks. 
"""
