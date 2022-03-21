from db.run_sql import run_sql
from models.player import Player

def save(player):
    sql = "INSERT INTO Player(name, gender, weight_kg) VALUES ( %s, %s, %s ) RETURNING id"
    values = [player.name, player.gender, player.weight_kg]
    results = run_sql( sql, values )
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