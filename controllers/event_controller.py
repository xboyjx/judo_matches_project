from flask import Flask, render_template, request, redirect, Blueprint

import repositories.event_repository as event_repository

events_blueprint = Blueprint("events", __name__)