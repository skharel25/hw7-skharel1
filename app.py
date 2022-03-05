from crypt import methods
import random
import time
import flask
from flask import jsonify
from flask_cors import CORS

app = flask.Flask(__name__)

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint("bp", __name__, template_folder="./static/react",)

# route for serving React page
@bp.route("/")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@bp.route("/api", methods=["POST", "GET"])
def API():
    ListofFacts = [
        "The first person ever convicted of speeding was going eight mph.",
        "The moon has moonquakes.",
    ]
    index = random.randint(0, 1)
    data = "Random Fact:", ListofFacts[index]
    return flask.jsonify(data)


app.register_blueprint(bp)


app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.run(debug=True)
