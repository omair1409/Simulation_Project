"""
This script is part of the Data science application for corteva
"""

#in this simulation, many assumptions been made for the model simplicity, gender ratio, pregenency period, time to harvest...etc.


# start with importing the required libraries 
import random
import matplotlib.pyplot as plt

#define the papramters per the problem instructions

initialPopulation = 50
infantMortality = 5
productivity = 5
disasterChance = 10
fertilityx = 18
fertilityy = 35
food = 0
peopleDict = []


# define class with two values gender ans age
# note that age is not set to be zero, because we need to initilize with ages btw (18, 50)

# based on my research, female ratio ~ 50% https://ourworldindata.org/gender-ratio so I am gonna assign 50% for a new person to be Female (and in the initilization of the simulation as well)
class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age


# for harvest anyone over eight can harvest 5 units, then if there's enough food some dies, each one need 1 unit for the whole year
def harvest(food, productivity):
    ablePeople = 0
    for person in peopleDict:
        if person.age > 8:
            ablePeople +=1
    food += ablePeople * productivity
    if food < len(peopleDict):
        del peopleDict[0:int(len(peopleDict)-food)]
        food = 0
    else:
        food -= len(peopleDict)
# we can add how many untis needed for each person, but since in our case here is 1, will keep it simple
    # food -= consumeUnit*len(peopleDict)


# here is the function with infantMortality, we can assign infantMortality == 0.0 to cover both cases 
# 1 in 5 women will become pregnant can be modeled also in a different way:
    # check the length of women between 18 and 35, then devide by 5 and assign pregnancy to them 
    # I added randomness here random.randint(0,5)==1

def reproduce(fertilityx, fertilityy, infantMortality):
    for person in peopleDict:
        if (person.gender == 1 and  person.age > fertilityx and  person.age < fertilityy and random.randint(0,5)==1 and random.randint(0,100)>infantMortality):
            peopleDict.append(Person(0))

# for the simple case
def reproduceSimple(fertilityx, fertilityy):
    for person in peopleDict:
        if (person.gender == 1 and  person.age > fertilityx and  person.age < fertilityy and random.randint(0,5)==1):
            peopleDict.append(Person(0))

#initilize the simulation for both cases       
def beginSim():
    for x in range(initialPopulation):
        peopleDict.append(Person(random.randint(18,50)))

# I am having this order harvest, age > 80 die, then reproduce
def runYear(food, productivity, fertilityx, fertilityy, infantMortality, disasterChance):
    harvest(food, productivity)
    for person in peopleDict:
        if person.age > 80:
            peopleDict.remove(person)
        else:
            person.age +=1
    reproduce(fertilityx, fertilityy, infantMortality)
    if random.randint(0,100)<disasterChance:
        del peopleDict[0:int(random.uniform(0.05,0.15)*len(peopleDict))]


# here is for the simple case without infantMortality
def runYearSimple(food, productivity, fertilityx, fertilityy):
    harvest(food, productivity)
    reproduceSimple(fertilityx, fertilityy)
    for person in peopleDict:
        if person.age > 80:
            peopleDict.remove(person)
        else:
            person.age +=1
yrsSimple=[]
yrs=[]
pop=[]
popSimple=[]
m=0
##########################################################
# Start Simulation for the all the assumoptions
beginSim()
while len(peopleDict)<100000 and len(peopleDict) > 1:
    yrs.append(m)
    pop.append(len(peopleDict))
    #runYearSimple(food, productivity, fertilityx, fertilityy)
    runYear(food, productivity, fertilityx, fertilityy, infantMortality, disasterChance)
    m+=1

peopleDict=[]

###########################################################
# Start the simulation for the simple case
beginSim()
while len(peopleDict)<100000 and len(peopleDict) > 1:
    yrsSimple.append(m)
    popSimple.append(len(peopleDict))
    runYearSimple(food, productivity, fertilityx, fertilityy)
    #runYear(food, productivity, fertilityx, fertilityy, infantMortality, disasterChance)
    m+=1

# plot Population vs Yrs for both cases 


plt.subplot(211) # row 1, col 2 index 1
plt.plot(yrs, pop)
plt.title("Population Growth with disaster and infantMortality")
plt.xlabel('Yrs')
plt.ylabel('Population')

plt.subplot(212) # index 2
plt.plot(yrsSimple, popSimple)
plt.title("Population Growth Simple Assumption")
plt.xlabel('Yrs')
plt.ylabel('Population')
plt.show()




