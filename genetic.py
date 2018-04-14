import random
import matplotlib.pyplot as plt
import math
import sys

plt.ion()

#config  here
num_of_islands = 5
limit = 100
number = 100
exit_num = 100000
population_number = 2000
mutate_precent = 0.10 

def get_random_point():
    res = []
    res.append(int(random.random()*limit))
    res.append(int(random.random()*limit))
    return res

def get_random_field(mode = 0):
    if mode == 0:
        res = []
        for i in range(number):
            res.append(get_random_point())
        return res
    else:
        test_sample = [[154, 185], [7, 266], [156, 52], [162, 223], [273, 174], [228, 282], [218, 75], [34, 87],
                       [124, 155], [279, 93], [201, 188], [101, 258], [266, 55], [106, 219], [230, 97], [176, 110],
                       [126, 167], [50, 223], [256, 289], [286, 227], [70, 263], [235, 84], [91, 131], [114, 17],
                       [131, 298], [229, 174], [46, 215], [76, 65], [57, 99], [71, 225], [16, 126], [112, 226],
                       [224, 161], [244, 154], [175, 9], [120, 291], [145, 41], [110, 265], [191, 42], [36, 213],
                       [45, 171], [281, 77], [155, 204], [82, 215], [269, 226], [71, 132], [135, 12], [41, 160],
                       [278, 131], [1, 81], [296, 244], [272, 168], [148, 64], [38, 202], [28, 2], [125, 283],
                       [229, 280], [156, 51], [51, 268], [107, 250], [48, 211], [227, 231], [257, 184], [171, 256],
                       [21, 273], [38, 89], [231, 105], [231, 211], [265, 273], [233, 258], [33, 290], [288, 131],
                       [146, 279], [59, 27], [141, 68], [170, 211], [293, 298], [21, 153], [17, 222], [152, 280],
                       [259, 57], [269, 279], [202, 23], [1, 208], [185, 9], [67, 79], [95, 291], [207, 130],
                       [190, 119], [198, 147], [54, 5], [19, 43], [48, 294], [290, 248], [90, 94], [76, 215],
                       [279, 132], [244, 88], [271, 4], [57, 164]]
        return test_sample[:]

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
    shift  = int(random.random()*len(parent1)/2)
    child = parent1[shift:int(len(parent1)/2)]
    for gen in parent2:
        if gen not in child: child.append(gen)
    return child

def select(population):
    population.sort(key=get_cost)
    return population[0:population_number]

adams = [get_random_field(mode = 1) for x in range(num_of_islands)] #first guy

populations = []

for pop in range(num_of_islands):
    populations.append([])
    for subject in range(population_number): #create first population
        populations[pop].append(adams[pop][:])
        mutate(populations[pop][-1],1)

generation = 0
last_cost = 0

while (True):
    generation +=1
    for pop in range(len(populations)):
        #mutate
        random.shuffle(populations[pop])
        for index in range(int(population_number*mutate_precent)):
            populations[pop].append(populations[pop][index][:])
            mutate(populations[pop][-1])
        # find boys and girls
        random.shuffle(populations[pop]) 
        #make love
        for index in range(len(populations[pop])):
            populations[pop].append(cross(populations[pop][index],
                                    populations[pop][population_number-index-1])
                            )
        populations[pop] = select(populations[pop])

        if generation % 100 == 1:
            plt.clf()
            plt.plot([el[0] for el in populations[0][0]],[el[1] for el in populations[0][0]]) 
            plt.show()
            plt.pause(0.1)
        # print (len(population))
        print('gen {}: pop: {}: {}'.format(generation,pop,get_cost(populations[pop][0])))

print ('done!')
plt.ioff()
plt.clf()
plt.plot([el[0] for el in population],[el[1] for el in population]) 
plt.show()