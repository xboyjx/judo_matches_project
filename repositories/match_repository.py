from db.run_sql import run_sql
from models.match import Match
import repositories.event_repository as event_repository
import repositories.player_repository as player_repository

def save(match):
    sql = "INSERT INTO matches ( player1_id, player2_id, event_id, winner ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [match.player1.id, match.player2.id, match.event.id, match.winner.id]
    results = run_sql( sql, values )
    match.id = results[0]['id']
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        player1 = player_repository.select(row['player1_id'])
        player2 = player_repository.select(row['player2_id'])
        event = event_repository.select(row['event_id'])
        winner = player_repository.select(row['winner'])
        match = Match(player1.id, player2.id, event.id, winner.id)
        matches.append(match)
    return matches
