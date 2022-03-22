from flask import Blueprint, Flask, render_template, request, redirect
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository
import repositories.event_repository as event_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/Latest-Matches")
def latest_matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches = matches)