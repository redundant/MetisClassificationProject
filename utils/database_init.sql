CREATE TABLE summoners(
    id char(63) NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE champions(
    id decimal NOT NULL,
    name char(63),

    PRIMARY KEY (id)
);

CREATE TABLE champion_masteries(
    summoner_id char(63) NOT NULL REFERENCES summoners(id),
    champion_id int NOT NULL REFERENCES champions(id),

    mastery_points decimal,

    PRIMARY KEY (champion_id, summoner_id)
);

CREATE TABLE matches (
    id decimal NOT NULL,

    side char(5),

    player0_id char(63) NOT NULL REFERENCES summoners(id),
    player0_role char(63),
    player0_champ decimal REFERENCES champions(id),
    player0_vs int,
    
    player1_id char(63) NOT NULL REFERENCES summoners(id),
    player1_role char(63),
    player1_champ decimal REFERENCES champions(id),
    player1_vs int,
    
    player2_id char(63) NOT NULL REFERENCES summoners(id),
    player2_role char(63),
    player2_champ decimal REFERENCES champions(id),
    player2_vs int,
    
    player3_id char(63) NOT NULL REFERENCES summoners(id),
    player3_role char(63),
    player3_champ decimal REFERENCES champions(id),
    player3_vs int,
    
    player4_id char(63) NOT NULL REFERENCES summoners(id),
    player4_role char(63),
    player4_champ decimal REFERENCES champions(id),
    player4_vs int,

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
