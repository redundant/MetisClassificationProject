import pandas as pd
import numpy as np

champion_data = pd.read_json("../data/championFull.json")

ids = []
names = []

for entry in champion_data["data"]:
    try:
        ids.append(entry["key"])
        names.append(entry["id"])

    except:
        break

pd.DataFrame.from_dict({"id":ids,"name":names}).to_csv("../data/champions.csv", index=False)