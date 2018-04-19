#Tahsin Islam Sakif
#20th April 2018
#CS 293B
#Homework Number 6

import csv
import numpy as np
import matplotlib.pyplot as plt

def open_file(fileName):
    try:
        arr=np.genfromtxt(fileName, delimiter=',', usecols=(1,2,3,4,5,6))
    except OSError:
        print("File not found")
        raise OSError

    return arr

def cost_per_student(nparrloans,nparrrecipients):
    nparrloanperstudent=(nparrloans*1000000000)/(nparrrecipients*1000000)
    return nparrloanperstudent
def read_labels(fileName):
    labels=[]
    try:
        labelFile=open(fileName,"r")
        for x in labelFile:
            temp=x.strip()
            temp=temp.title()
            labels.append(temp)
        labelFile.close()
    except IOError:
        print("label file not found")
    return labels
        
def display_amounts_whole(npdata,labels,title):
    plt.pie(npdata,labels=labels)
    plt.title(title)
    plt.show()
    
def write_averages_to_file(fileName,labels,averages):
    if(len(labels)==len(averages)):
        try:
            file=open(fileName,"w",newline='')
            csvFile=csv.writer(file,delimiter=',')
            for x in range(len(labels)):
                csvFile.writerow([labels[x],averages[x]])
            file.close()
        except IOError:
            print("Output file not valid")
            raise IOError
    else:
        print("labels do not match averages")



def main():
    loanamts=open_file("Loan_amounts_by_type_data.csv")
    population=open_file("Loan_amounts_by_type_number.csv")
    dataLabels=read_labels("loan_types.txt")
    calculation=cost_per_student(loanamts,population)
    costperstudent=np.around(np.mean(calculation,axis=0))
    display_amounts_whole(population[-1,:],dataLabels,"Loan Amounts by Type\n4th Quarter 2017")
    write_averages_to_file("average_award_amount_per_student.csv",dataLabels,costperstudent.tolist())


if __name__=='__main__':
    main()
"""
12 a) The outstanding balance of subsidized loans is about half of the unsubsidized
amounts because the government is paying for the tax interest for one while
the other keeps increasing daily.

b) The outstanding balance is increasing because the universities are
charging more money from students. It will keep growing unless something
is done to lower these high costs.

"""
    
    
    

            

            
