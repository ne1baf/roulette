from bs4 import BeautifulSoup as BS
from pyparsing import Literal, quotedString, removeQuotes, delimitedList
import requests
import pickle
import json
from datetime import datetime
import time
import numpy as np
import random
import pandas as pd
from tqdm import tqdm

rolls = []

for seed in tqdm(range(1900, 2234)):
    filename = "data/seed_" + str(seed) + ".json"
    data = pd.read_json(filename)
    df = pd.json_normalize(data["rolls"])
    rolls = np.concatenate([rolls, df.coin])

np.savetxt("rolls_simpler.txt", rolls[None], fmt="%d", delimiter=",")
print("\n   nombre de rolls : ", len(rolls))
