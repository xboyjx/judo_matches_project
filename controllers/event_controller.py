from flask import Flask, render_template, request, redirect, Blueprint

import repositories.event_repository as event_repository
import repositories.match_repository as match_repository

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/events")
def events():
    events = event_repository.select_all()
    return render_template("events/index.html", events = events)

@events_blueprint.route("/events/<id>")
def show(id):
    matches = match_repository.select_all()
    event = event_repository.select(id)
    return render_template("events/show.html", matches = matches, event = event)

