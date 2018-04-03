"""
Tahsin Islam Sakif
1 February 2018
CS 293B
Homework 1
"""

#Month in relation to Days PRT in Service

JanuaryService=22
FebruaryService=24
MarchService=20
AprilService=24
MayService=8
JuneService=26
JulyService=25
AugustService=26
SeptemberService=24

#Month in relation to Number of Passengers 

JanuaryPassenger=223012
FebruaryPassenger=256658
MarchPassenger=197962
AprilPassenger=222675
MayPassenger=28914
JunePassenger=31990
JulyPassenger=48622
AugustPassenger=241760
SeptemberPassenger=359866

#Calculation of Passengers per day for the number of days the PRT was in service

JanuaryPassPerDay=JanuaryPassenger/JanuaryService
print("The passengers per day for January was: %d"%(JanuaryPassPerDay))
FebruaryPassPerDay=FebruaryPassenger/FebruaryService
print("The passengers per day for February was: %d"%(FebruaryPassPerDay))
MarchPassPerDay=MarchPassenger/MarchService
print("The passengers per day for March was: %d"%(MarchPassPerDay))
AprilPassPerDay=AprilPassenger/AprilService
print("The passengers per day for April was: %d"%(AprilPassPerDay))
MayPassPerDay=MayPassenger/MayService
print("The passengers per day for May was: %d"%(MayPassPerDay))
JunePassPerDay=JunePassenger/JuneService
print("The passengers per day for June was: %d"%(JunePassPerDay))
JulyPassPerDay=JulyPassenger/JulyService
print("The passengers per day for July was: %d"%(JulyPassPerDay))
AugustPassPerDay=AugustPassenger/AugustService
print("The passengers per day for August was: %d"%(AugustPassPerDay))
SeptemberPassPerDay=SeptemberPassenger/SeptemberService
print("The passengers per day for September was: %d\n"%(SeptemberPassPerDay))

#7. Calculation of whether or not January's passenger per day was above or below average

Average=7898

if JanuaryPassPerDay>Average:
    print("January was above average")
else:
        print("January was below average")

#8. Calculation of whether June or July were above or below average

if (JunePassPerDay or JulyPassPerDay) > Average:
    print("June or July was above average")
else:
    print("June and July were both below average")

"""
9. a)
The main advantage of the PRT is that it is free for all WVU students and employees. The PRT
is a great resource for everyone to get from one campus to another in a quick and easy way.
Those that do not have their own means of transporation such as a car will be disadvantaged to
get to class, and it will be an additional cost in their daily lives to pay for $0.50 per trip.
The costs will easily add up because students use the PRT frequently every day. Financially, this
will be bad for the people who rely on the PRT. However, for the university this will be a huge amount
of profit, as they will make a lot of money every day which could go into the school's funding. However,
many will stop using the PRT altogether because of this change and long term wise the usage of the
PRT will become scarce as everyone will use other means of transporation, such as buses which are free.
Short term the university will make some money but overall will limit the usage of the transporation
vehicle system.
"""



