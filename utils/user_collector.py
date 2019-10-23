import pandas as pd 
import data_collection
import cassiopeia as cass
import os.path

update = os.path.exists("../data/user_data.csv")

if update:
    previous_data = pd.read_csv("../data/user_data.csv")

match_data = pd.read_csv("../data/match_data.csv")

ids = set()

for i in range(5):
    for id in match_data["player"+str(i)+"_id"]:
        ids.add(id)

if update:
    old_users = set(previous_data["id"].unique())
    ids.remove(old_users)

users = [data_collection.get_user_role_stats(cass.get_summoner(account_id=id, region="NA"), 10) for id in ids]

data = pd.concat([pd.DataFrame.from_dict(user) for user in users])

if update:
    data = pd.concat([data,previous_data])

data.to_csv("../data/user_data.csv", index=False)