from flask import Blueprint, Flask, render_template, request, redirect

import repositories.player_repository as player_repository
import repositories.match_repository as match_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players = players)

@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select(id)
    matches = match_repository.select_all()
    return render_template("players/show.html", player = player, matches = matches)