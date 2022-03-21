from flask import Blueprint, Flask, render_template, request, redirect

import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)