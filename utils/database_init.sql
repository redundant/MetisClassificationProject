CREATE TABLE summoners(
    id char(63) NOT NULL,

    top_wins int,
    jun_wins int,
    mid_wins int,
    adc_wins int,
    sup_wins int,

    top_losses int,
    jun_losses int,
    mid_losses int,
    adc_losses int,
    sup_losses int,

    PRIMARY KEY (id)
);

CREATE TABLE champions(
    id int NOT NULL,
    name char(63),

    PRIMARY KEY (id)
);

CREATE TABLE champion_masteries(
    champion_id int NOT NULL REFERENCES champions(id),
    summoner_id char(63) NOT NULL REFERENCES summoners(id),

    mastery_points int,

    PRIMARY KEY (champion_id, summoner_id)
);

CREATE TABLE matches (
    id int NOT NULL,
    league char(63),

    side char(5),
    top_id char(63) NOT NULL REFERENCES summoners(id),    
    jun_id char(63) NOT NULL REFERENCES summoners(id),
    mid_id char(63) NOT NULL REFERENCES summoners(id),
    adc_id char(63) NOT NULL REFERENCES summoners(id),
    sup_id char(63) NOT NULL REFERENCES summoners(id),

    top_champ int NOT NULL REFERENCES champions(id),
    jun_champ int NOT NULL REFERENCES champions(id),
    mid_champ int NOT NULL REFERENCES champions(id),
    adc_champ int NOT NULL REFERENCES champions(id),
    sup_champ int NOT NULL REFERENCES champions(id),
   
    top_vs int,
    jun_vs int,
    mid_vs int,
    adc_vs int,
    sup_vs int,
    
    top_cs_10 float,
    top_cs_20 float,
    top_xp_10 float,
    top_xp_20 float,
    
    jun_cs_10 float,
    jun_cs_20 float,
    jun_xp_10 float,
    jun_xp_20 float,

    mid_cs_10 float,
    mid_cs_20 float,
    mid_xp_10 float,
    mid_xp_20 float,
 
    adc_cs_10 float,
    adc_cs_20 float,
    adc_xp_10 float,
    adc_xp_20 float,
    
    sup_cs_10 float,
    sup_cs_20 float,
    sup_xp_10 float,
    sup_xp_20 float,
    
    first_brick bool,
    first_blood bool,
    first_herald bool,
    first_dragon bool,
    first_baron bool,
    first_inhib bool,
    
    num_dragons int,
    num_barons int,
    num_towers int,
    num_inhibs int,

    result bool,

    PRIMARY KEY (id)
);
