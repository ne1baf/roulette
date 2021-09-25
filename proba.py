import pickle
import json
from datetime import datetime
import time
import numpy as np
import random
import pandas as pd
from tqdm import tqdm

##################################################################################################
'''
The idea is that although online roulette is supposedly random, the odds aren't roughly 

''' FUNCTIONS '''
#those functions will be used to fill in the probability array and make the whole code cleaner
'''
    Basically, our function takes a certain 


''' INITIALIZING PHASE '''



#retrieving rolls from the file that contains them
rolls = np.loadtxt("rolls_simpler.txt", delimiter=",", dtype=int)

#creating the array that will contain the probabilities
probabilities = np.empty(9,10)

#initializing variables : streak length = 0 because it's the first roll and the current roll = first roll
curr_streak_len = 0
curr_roll = rolls[0]

for roll in rolls[1:] : 
    