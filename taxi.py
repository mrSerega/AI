import gym
import numpy as np
import time
import os
from tqdm import tqdm

def sortFunc(el):
    return el[-1]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

view = 0
agnets = 100
trys = 100

env = gym.make("Taxi-v2")
n_actions = env.action_space.n
n_states = env.observation_space.n
# env.render()

policy  = [[1/n_actions for _ in range(n_actions)] for _ in range(n_states)]

# print(policy)

observation = env.reset()
# print('----')

for t in tqdm(range(trys)):

    log = []
    rewards = []

    for agent in range(agnets):
        tmp = []
        rewards = 0
        observation  = env.reset()
        while True:
            
            action = np.random.choice(n_actions, p = policy[observation])
            pair = [observation,action]
            observation, reward , done, info = env.step(action)
            if reward > -2: tmp.append(pair)
            if reward > 0: 
                for c in range(100): 
                    tmp.append(pair)
            rewards+=reward            

            if done:
                if rewards >= -250: log.append([tmp,rewards])
                break
            

    # print (log)
    log.sort(key = sortFunc)
    log.reverse()
    # print ([el[-1] for el in log])

    data = [[0,0,0,0,0,0] for _ in policy]
    for agentLog in log:
        for el in agentLog[0]:
            data[el[0]][el[1]]+=1
    for pos in range(len(data)):
        for p in range(n_actions):
            data[pos][p]+=1
    for pos in range(len(data)):
        s = sum(data[pos])
        for p in range(n_actions):
            data[pos][p]/=s
    policy=data[:]

# print (log)

# final test

rewards = 0
obervation = env.reset()

# input()

r = []

for t in range(5):
    while True:   
        action = np.random.choice(n_actions, p = policy[observation])
        # action = policy[obervation]
        observation, reward , done, info = env.step(action)
        rewards+=reward
        print ('score: {}/ cost fo currentaction {}'.format(rewards,reward))

        # tmp.append([last_observation,action])
        # last_observation = observation

        cls()
        env.render()
        time.sleep(0.01)

        if done:
            # log.append([tmp,rewards])
            break

    r.append(rewards)
print (r)