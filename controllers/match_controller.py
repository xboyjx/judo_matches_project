from flask import Blueprint, Flask, render_template, request, redirect
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)