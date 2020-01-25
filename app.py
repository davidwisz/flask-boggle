from flask import Flask, render_template, request, redirect, flash, session, jsonify
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

# create instance of Boggle class
boggle_game = Boggle()


@app.route("/")
def begin():
    # use boggle_game method to instantiate a board
    boggle_board = boggle_game.make_board()
    # pass the board to Jinja template
    session["board"] = boggle_board
    session['words'] = []
    session['score'] = 0

    return render_template("index.html", board=boggle_board)


@app.route("/word-check", methods=["POST"])
def post_word():

    word = request.json['word']
    word_exists = True if word in boggle_game.words else False
    if word_exists:
        word_on_board = True if boggle_game.check_valid_word(
            session['board'], word) == "ok" else False

        if word_on_board is True:
            # Add word to words in session
            words_list = session['words']
            words_list.append(word)
            session['words'] = words_list

            # Add points to score in session
            word_score = len(word)
            session['score'] += word_score

            # Update result dictionary
            result = {'result': 'ok', 'word': word, 'score': word_score}
        else:
            # Update result dictionary
            result = {'result': 'not-on-board', 'word': word}
    else:
        # Update result dictionary
        result = {'result': 'not-a-word', 'word': word}

    print("words in session", session['words'])
    print("WORD DATA", word)
    return jsonify(result)
