import gym
import time,sys
import numpy as np
import os

debug = True
pre = [0] * 128
def print_update(obs: np.ndarray):
    os.system('clear')
    global pre
    i = 0
    for _ in range(8):
        for _ in range(16):
            tar = str(obs[i])
            res = f'{tar:>3}'
            if pre[i] != obs[i]:
                res = '\x1b[6;30;42m' + res + '\x1b[0m'
            print(res, end=' ')
            i += 1
        print()
    pre = obs
    # input("shit")

env = gym.make('Frostbite-ramDeterministic-v0')
for i_episode in range(20):
    observation = env.reset()
    pre_act = 0
    for t in range(1000):
        env.render()
        if debug:
            print_update(observation)
        action = env.action_space.sample() # action space 0-17, inclusive
        # print(type(env.action_space))
        # print(env.action_space)
        custom_act = int(input("0-17: ") or pre_act)
        pre_act = custom_act
        observation, reward, done, info = env.step(custom_act)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
