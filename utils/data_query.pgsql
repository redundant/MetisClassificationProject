SELECT

matches.player0_role,
matches.player0_vs,
t1.mastery_points as player0_mastery, 

matches.player1_role,
t2.mastery_points as player1_mastery,
matches.player1_vs,

matches.player2_role,
matches.player2_vs,
t3.mastery_points as player2_mastery,

matches.player3_role,
matches.player3_vs,
t4.mastery_points as player3_mastery,

matches.player4_role,
matches.player4_vs,
t5.mastery_points as player4_mastery,

matches.side,

matches.first_brick,
matches.first_blood,
matches.first_dragon,
matches.first_herald,
matches.first_baron,
matches.first_inhib,

matches.num_towers,
matches.num_dragons,
matches.num_barons,
matches.num_inhibs

FROM matches
LEFT JOIN champion_masteries t1
ON matches.player0_id = t1.summoner_id
AND matches.player0_champ = t1.champion_id
INNER JOIN champion_masteries t2
ON matches.player1_id = t2.summoner_id
AND matches.player1_champ = t2.champion_id
LEFT JOIN champion_masteries t3
ON matches.player2_id = t3.summoner_id
AND matches.player2_champ = t3.champion_id
LEFT JOIN champion_masteries t4
ON matches.player3_id = t4.summoner_id
AND matches.player3_champ = t4.champion_id
LEFT JOIN champion_masteries  t5
ON matches.player4_id = t5.summoner_id
AND matches.player4_champ = t5.champion_id
LIMIT 10;