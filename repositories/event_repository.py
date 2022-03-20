from db.run_sql import run_sql
from models.event import Event

def save(event):
    sql = "INSERT INTO events(name, location, date) VALUES ( %s, %s, %s ) RETURNING id"
    values = [event.name, event.location, event.date]
    results = run_sql( sql, values )
    event.id = results[0]['id']
    return event