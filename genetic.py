import random
import matplotlib.pyplot as plt
import math
import sys

plt.ion()

#config  here
limit = 100
number = 15
exit_num = 100000

def get_random_point():
    res = []
    res.append(int(random.random()*limit))
    res.append(int(random.random()*limit))
    return res

def get_random_filed():
    res = []
    for i in range(number):
        res.append(get_random_point())
    return res

def get_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def get_cost(filed):
    sum = 0
    for index in range(len(filed)-1):
        sum += get_distance(filed[index],filed[index+1])
    return sum

def do_random(filed, mode = 0):
    if mode == 0:
        first = int(random.random()*len(filed)) - 1
        second = int(random.random()*len(filed)) - 1

        filed[first], filed[second] = filed[second], filed[first]
    elif mode == 1:
        random.shuffle(filed)

filed = get_random_filed()

last_cost = sys.float_info.max
last_state = filed[:]
last_state_index = 0
index = 0

while ((index - last_state_index) < exit_num):
    index +=1
    last_state = filed[:]
    do_random(filed)
    current_cost = get_cost(filed)
    if current_cost >= last_cost: filed = last_state[:]
    else:
        last_state_index = index
        last_cost= current_cost
        plt.clf()
        plt.plot([el[0] for el in filed],[el[1] for el in filed]) 
        plt.show()
        plt.pause(0.1)
    print ('best solution: {}, new solutin: {}'.format(last_cost,current_cost))

print ('done!')
plt.ioff()
plt.clf()
plt.plot([el[0] for el in filed],[el[1] for el in filed]) 
plt.show()