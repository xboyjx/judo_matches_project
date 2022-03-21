from flask import Flask, render_template, request, redirect, Blueprint

import repositories.event_repository as event_repository

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/events")
def events():
    events = event_repository.select_all()
    return render_template("events/index.html", events = events)
