import data_collection
import pandas as pd
import cassiopeia as cass
import os.path

update = os.path.exists("../data/mastery.csv")

if update:
    previous_data = pd.read_csv("../data/mastery.csv")

match_data = pd.read_csv("../data/match_data.csv")

ids = set()

for i in range(5):
    for pair in zip(match_data["player"+str(i)+"_id"],match_data["player"+str(i)+"_champ"]):
        ids.add(pair)

if update:
    for pair in zip(previous_data["summoner_id"], previous_data["champion_id"]):
        ids.discard(pair)

masteries = []


sample = list(ids)

for pair in sample:

    summoner = cass.get_summoner(account_id = pair[0], region = "NA")
    champion = cass.Champion(id=pair[1],region="NA")
    masteries.append(data_collection.get_user_champion_mastery(summoner,champion))

data = pd.concat([pd.DataFrame.from_dict(mastery) for mastery in masteries])

if update:
    data = pd.concat([data,previous_data])

data = data.drop_duplicates(subset=["summoner_id","champion_id"])

data.to_csv("../data/mastery.csv", index=False)
