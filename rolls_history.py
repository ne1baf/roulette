from bs4 import BeautifulSoup as BS
from pyparsing import Literal, quotedString, removeQuotes, delimitedList
import requests
import pickle
import json
from datetime import datetime
import time
import random
from tqdm import tqdm


for seed in tqdm(range(1900, 2234)):
    data = {}
    data["rolls"] = []
    time.sleep(random.uniform(1.5, 2.6))
    rolls_data = requests.get(
        "https://csgoempire.com/api/v2/metadata/roulette/history?seed=" + str(seed)
    )

    allItems = rolls_data.content
    allItems = json.loads(allItems)
    allItems = allItems["rolls"]

    # print(allItems[0]["coin"])
    for i in range(len(allItems)):
        data["rolls"].append(
            {
                "date": allItems[i]["time"],
                "coin": 1
                if allItems[i]["coin"].strip() == "ct"
                else 2
                if allItems[i]["coin"].strip() == "t"
                else 0,
                "roll": allItems[i]["roll"],
            }
        )

    with open(f"data/seed_{seed}.json", "w") as outfile:
        json.dump(data, outfile)
    '''
    item_df = pd.DataFrame.from_dict(data_point, orient="index")
    output_name = "data/watch/pickle/" + item.split(".pkl")[0] + ".csv"
    item_df.transpose().to_csv(output_name)
    '''
