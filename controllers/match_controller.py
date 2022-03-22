from flask import Blueprint, Flask, render_template, request, redirect
from controllers.player_controller import players
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository
import repositories.event_repository as event_repository
from models.match import Match

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches = matches)

@matches_blueprint.route("/add-new-match", methods=['GET'])
def new_match():
    players = player_repository.select_all()
    events = event_repository.select_all()
    return render_template("matches/new.html", players = players, events = events)

@matches_blueprint.route("/matches", methods=['POST'])
def create_match():
    player1_id = request.form['player1_id']
    player2_id = request.form['player2_id']
    event_id = request.form['event_id']
    winner = request.form ['winner']
    player1 = player_repository.select(player1_id)
    player2 = player_repository.select(player2_id)
    event = event_repository.select(event_id)
    if winner == "player1":
        winner = player1
    else:
        winner = player2
    match = Match(player1, player2, event, winner)
    match_repository.save(match)
    return redirect('/matches')
