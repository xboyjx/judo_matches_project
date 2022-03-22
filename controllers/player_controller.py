from flask import Blueprint, Flask, render_template, request, redirect

import repositories.player_repository as player_repository
import repositories.match_repository as match_repository
from models.player import Player

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

@players_blueprint.route("/players/new", methods=['GET'])
def new_player():
    return render_template("players/new.html")

@players_blueprint.route("/players", methods=['POST'])
def create_player():
    name = request.form['name']
    gender = request.form['gender']
    weight_kg = request.form['weight_kg']
    player = Player(name, gender, weight_kg)
    player_repository.save(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/remove")
def remove_player(id):
    player_repository.delete(id)
    return redirect("/players")