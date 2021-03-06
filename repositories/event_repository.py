from db.run_sql import run_sql
from models.event import Event
from models.player import Player

def save(event):
    sql = "INSERT INTO events(name, location, date) VALUES ( %s, %s, %s ) RETURNING id"
    values = [event.name, event.location, event.date]
    results = run_sql( sql, values )
    event.id = results[0]['id']
    return event

def select_all():
    events = []

    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        event = Event(row['name'], row['location'], row['date'], row['id'])
        events.append(event)
    return events

def select(id):
    location = None
    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        event = Event(result['name'], result['location'], result['date'], result['id'] )
    return event

def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM events WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def players(event):
    players = []

    sql = "SELECT * FROM players INNER JOIN matches ON matches.player1_id = player1.id or matches.player2_id = player2.id  WHERE matches.event_id =%s;"
    values = [event.id]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['name'], row['gender'], row['weight_kg'], row['id'])
        players.append(player)