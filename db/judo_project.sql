DROP TABLE matches;
DROP TABLE events;
DROP TABLE players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    gender VARCHAR(255),
    weight_kg INT
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR (255),
    date VARCHAR (255)
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    player1_id INT REFERENCES players(id) ON DELETE CASCADE,
    player2_id INT REFERENCES players(id) ON DELETE CASCADE,
    event_id INT REFERENCES events(id) ON DELETE CASCADE,
    winner INT REFERENCES players(id) ON DELETE CASCADE
)