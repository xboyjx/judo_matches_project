from db.run_sql import run_sql
from models.player import Player
from models.event import Event

def save(player):
    sql = "INSERT INTO players(name, gender, weight_kg) VALUES ( %s, %s, %s ) RETURNING id"
    values = [player.name, player.gender, player.weight_kg]
    results = run_sql(sql, values )
    player.id = results[0]['id']
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['name'], row['gender'], row['weight_kg'], row['id'])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['name'], result['gender'], result['weight_kg'], result['id'] )
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def events(player):
    events = []

    sql = "SELECT * FROM events INNER JOIN matches ON matches.event_id = events.id WHERE matches.player1_id =%s or matches.player2_id = %s;"
    values = [player.id, player.id]
    results = run_sql(sql, values)

    for row in results:
        event = Event(row['name'], row['location'], row['date'], row['id'])
        events.append(event)