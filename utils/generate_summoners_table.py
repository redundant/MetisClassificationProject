import pandas as pd 

match_data = pd.read_csv("../data/match_data.csv")

names = set()

for i in range(5):
    names = names.union(set(match_data["player"+str(i)+"_id"]))

table = {"summoner_id":list(names)}

summoners = pd.DataFrame.from_dict(table)

summoners.to_csv("../data/names.csv", index=False)