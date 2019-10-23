import pandas as pd 
import data_collection
import cassiopeia as cass
import os.path

update = os.path.exists("../data/match_data.csv")

if update:
    previous_data = pd.read_csv("../data/match_data.csv")

match_ids = set()

grandmaster = cass.get_grandmaster_league(region="NA", queue=cass.data.Queue.ranked_solo_fives)

for account in grandmaster:
    summoner = account.summoner

    for match in summoner.match_history[:5]:
            if match.queue == cass.data.Queue.ranked_solo_fives:
                match_ids.add(match.id)

if update:
    old_matches = set(previous_data["id"].unique())
    match_ids = match_ids - old_matches

matches = [data_collection.get_match_data(id) for id in match_ids]

match_data = pd.concat([pd.DataFrame.from_dict(match) for match in matches])

if update:
    match_data = pd.concat([previous_data, match_data])

match_data.to_csv("../data/match_data.csv", index=False)