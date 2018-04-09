import random
import matplotlib.pyplot as plt
import math
import sys

plt.ion()

#config  here
limit = 100
number = 15
exit_num = 100000
population_number = 2000
mutate_precent = 0.10 

def get_random_point():
    res = []
    res.append(int(random.random()*limit))
    res.append(int(random.random()*limit))
    return res

def get_random_field():
    res = []
    for i in range(number):
        res.append(get_random_point())
    return res

def get_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def get_cost(field):
    sum = 0
    for index in range(len(field)-1):
        sum += get_distance(field[index],field[index+1])
    return sum

def mutate(field, mode = 0):
    if mode == 0:
        first = int(random.random()*len(field)) - 1
        second = int(random.random()*len(field)) - 1

        field[first], field[second] = field[second], field[first]
    elif mode == 1:
        random.shuffle(field)

def cross(parent1, parent2):
    child = parent1[0:len(parent1)/2]
    for gen in parent2:
        if gen not in child: child.append(gen)
    return child

def select(population):
    population.sort(key=get_cost)
    return population[0:population_number]

adam = get_random_field() #first guy

population = []

for subject in range(population_number): #create first population
    population.append(adam[:])
    mutate(population[-1],1)

generation = 0
last_cost = 0

while (generation < 50):
    generation +=1
    #mutate
    random.shuffle(population)
    for index in range(int(population_number*mutate_precent)):
        population.append(population[index][:])
        mutate(population[-1])
    # find boys and girls
    random.shuffle(population) 
    #make love
    for index in range(len(population)):
        population.append(cross(population[index],
                                population[population_number-index-1])
                        )
    population = select(population)

    if last_cost != get_cost(population[0]):
        plt.clf()
        plt.plot([el[0] for el in population[0]],[el[1] for el in population[0]]) 
        plt.show()
        plt.pause(0.1)
        last_cost = population[0]
    # print (len(population))
    print('gen {}: {}'.format(generation,get_cost(population[0])))

print ('done!')
plt.ioff()
plt.clf()
plt.plot([el[0] for el in population],[el[1] for el in population]) 
plt.show()