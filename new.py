import gym
import numpy as np
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

view = 0
agnets = 1000

env = gym.make("FrozenLake-v0")
n_actions = env.action_space.n
n_states = env.observation_space.n
# env.render()

policy  = [[1/n_actions for _ in range(n_actions)] for _ in range(n_states)]

# print(policy)

observation = env.reset()
# print('----')

while True:

    log = []

    for agent in range(agnets):
        tmp = []
        last_observation = 0

        observation = env.reset()
        while True:
            
            action = np.random.choice(n_actions, p = policy[observation])
            observation, reward , done, info = env.step(action)

            tmp.append([last_observation,action])
            last_observation = observation

            if view:
                cls()
                env.render()
                time.sleep(1)

            if reward > 0:
                # print ('!!!!!!!')
                log.append(tmp[:])

            if done:
                break
    # print('---')
    print('{}/{}'.format(len(log),agnets)) 
    # print(policy)
    data = [[0,0,0,0] for _ in policy]
    # print (data)
    for agentLog in log:
        for el in agentLog:
            data[el[0]][el[1]]+=1
    # print(data)
    for pos in range(len(data)):
        for p in range(4):
            data[pos][p]+=1
    # print (data)
    for pos in range(len(data)):
        s = sum(data[pos])
        for p in range(4):
            data[pos][p]/=s
    # print(data)
    policy=data[:]
    # break
