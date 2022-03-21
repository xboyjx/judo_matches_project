from flask import Flask, render_template

from controllers.event_controller import events_blueprint
from controllers.match_controller import matches_blueprint
from controllers.player_controller import players_controller

app = Flask(__name__)

app.register_blueprint(events_blueprint)
app.register_blueprint(matches_blueprint)
app.register_blueprint(players_blueprint)

@app.route('/')
def home():
    return render_template('home/index.html')

if __name__ == '__main__':
    app.run(debug=True)