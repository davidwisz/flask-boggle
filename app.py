from flask import Flask, render_template, request, redirect, flash, session
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

#create instance of Boggle class
boggle_game = Boggle()

@app.route("/")
def begin():
    # use boggle_game method to instantiate a board
    boggle_board = boggle_game.make_board()
    # pass the board to Jinja template
    return render_template("index.html", board=boggle_board)
