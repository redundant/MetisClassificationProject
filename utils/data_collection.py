import cassiopeia as cass
import pandas as pd 
import numpy as np

def get_match_data(match_id, region="NA"):
    """Return LoL match data from the API. At random chooses red or blue team to prevent any autocorrelation of data.

    Keyword arguments:
    match_id -- the league api match data
    region -- the region to draw from (default NA)

    Returns:
    A tuple of:

    match_id -- same as argument
    league -- Challenger,master,etc

    side -- red or blue side
    top_id -- the account id of the top laner on this side
    jun_id -- jungler
    mid_id -- mid laner
    adc_id -- bot carry
    sup_id -- support

    top_champ -- the champion id played top
    etc

    top_vs -- the vision score top
    etc

    top_cs_10 -- top cs difference at 10
    top_cs_20 -- same at 20
    top_xp_10 -- xp diff at 10
    top_cs_20 -- same at 20

    etc for other roles

    first_brick -- boolean for first tower
    first_blood -- first blood
    etc for herald, dragon, baron, inhib

    num_dragons -- number of dragons
    etc for barons, towers, inhibs

    result -- 1 for win 0 for loss
    """

    pass

def get_user_role_stats(summoner):
    """For the given userid, get ranked role distribution and winrates

    Keyword arguments:
    summoner -- a cass summoner object

    Returns:
    A tuple of:

    user_id -- the user_id from riot, a string 
    top_wins--number of games won top this season
    etc

    top_losses -- games lost as top this season
    etc
    """
    top_wins = 0
    jun_wins = 0
    mid_wins = 0
    adc_wins = 0
    sup_wins = 0

    top_total = 0
    jun_total = 0
    mid_total = 0
    adc_total = 0
    sup_total = 0

    match_hist = summoner.match_history
    ranked_hist = match_hist.filter(lambda m: m.queue == cass.data.Queue.ranked_solo_fives)

    for m in ranked_hist:
        player = m.participants[summoner.name]
        
        if player.lane == cass.data.Lane.top_lane:
            top_wins += player.team.win
            top_total += 1
            continue
        
        if player.lane == cass.data.Lane.jungle:
            jun_wins += player.team.win
            jun_total += 1
            continue

        if player.lane == cass.data.Lane.mid_lane:
            mid_wins += player.team.win
            mid_total += 1
            continue

        if player.lane == cass.data.Lane.bot_lane:
            if player.role == cass.data.Role.duo_carry:
                adc_wins += player.team.win
                adc_total += 1 
                continue

            elif player.role == cass.data.Role.duo_support:
                sup_wins += player.team.win
                sup_total += 1
                continue



    return (summoner.account_id,top_wins,jun_wins,mid_wins,adc_wins,sup_wins,top_total-top_wins,jun_total-jun_wins,mid_total-mid_wins,adc_total-adc_wins,sup_total-sup_wins)

def get_user_champion_mastery(summoner, champion):
    """For the given user_id and champion_id, get mastery points

    Keyword arguments:
    summoner -- a cass summoner object
    champion_id -- a cass champion object
    
    Returns:
    A tuple of:

    user_id -- the riot account id, a string
    champion_id -- the riot champion id, an int
    mastery_points -- the integer total of mastery points
    """

    points = summoner.champion_masteries[champion.name].points
    user_id = summoner.account_id
    champion_id = champion.id

    return (user_id, champion_id, points)