from flask import Flask, render_template, url_for, request, session, redirect, escape
import pandas as pd
import random
from functions import first_draw, second_draw, check_profit
from deck import deck
from label import DECK_ORIGINAL, str_BET_TO_HIGH, str_TOO_YOUNGER

app = Flask(__name__)
app.secret_key = "OUIJDANE_EL_IDRISSI_RIOUI"

@app.route('/')
def homepage():
    return render_template('launcher.html')

@app.route('/', methods=['POST'])
def wallet():
    session['wallet'] = request.form['wallet']
    session['pseudo'] = request.form['pseudo']
    session['error-form'] = False
    if int(request.form['age']) <= 18:
        session['error-form'] = str_TOO_YOUNGER
        return render_template('launcher.html')

    session['age'] = request.form['age']
    return redirect(url_for('board'))

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/board', methods=['POST'])
def get_first_draw():
    session["bet"] = request.form['bet']
    session['bet-to-hight'] = False
    if int(session["wallet"]) < int(session["bet"]):
        session['bet-to-hight'] = str_BET_TO_HIGH
        return render_template('board.html')

    session["wallet"] = int(session["wallet"]) - int(session["bet"])
    draw, deck = first_draw(DECK_ORIGINAL)
    session['first-draw'] = draw
    session['deck'] = deck
    return redirect(url_for('game_round'))

@app.route('/round')
def game_round():
    return render_template('round.html')

@app.route('/round', methods=['POST'])
def get_second_draw():
    hand = []
    for key in request.form:
        hand.append(escape(key))
    hand, deck = second_draw(session['deck'], 5 - len(hand), hand)
    
    is_winner, profit, result = check_profit(hand, int(session["bet"]))
    session["wallet"] = session["wallet"] + int(profit)
    session["message"] = result
    session["is-winner"] = is_winner

    if int(session["wallet"]) == 0:
        session["is-winner"] = False
    return  render_template('result.html', second_draw=hand)