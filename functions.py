import pandas as pd
import random
from label import CARD_T, CARD_J, CARD_Q, CARD_K, CARD_A, R_FLUSH, STRAIGHT_FLUSH, FOAK, FULL_HOUSE, FLUSH, STRAIGHT, TOAK, TP, OP, LOOSE

def first_draw(deck):
    draw = random.sample(deck, 5)
    for i in draw:
        deck.remove(i)
    return draw, deck

def draw(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck

def second_draw(deck, nb, cards):
    for _ in range(nb):
        card, deck = draw(deck)
        cards.append(card)
    return cards, deck

def new_hand(draw):
    dic = {}
    keys = [1,2,3,4,5]
    value = []
    color = []
    for i,k in zip(draw, keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        value.append(dic[key][0])
        color.append(dic[key][1])
    return value, color

def card_design(liste):
    for e,i in zip(liste, range(0,5)):
        try:
            liste[i] = int(e)
        except:
            if e == CARD_J:
                liste[i] = 11
            elif e == CARD_Q:
                liste[i] = 12
            elif e == CARD_K:
                liste[i] = 13
            elif e == CARD_A:
                liste[i] = 1
            else:
                continue
    return liste

def royal_flush(draw):
    winning_value = [CARD_T,CARD_J,CARD_Q,CARD_K,CARD_A]
    value, color = new_hand(draw)
    if sorted(winning_value) == sorted(value) and color.count(couleur[0]) == 5:
        return True
    else:
        return False

def straight_flush(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    value = sorted(value)
    straight = []
    for e, i in zip(value[0:-1], range(len(value)-1)):
        if e+1 == value[i+1]:
            straight.append('True')
        if straight.count('True') == 4 and color.count(color[0]) == 5:
            return True
        else:
            return False

def foak(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    new_value = pd.Series(value)
    uniques = new_value.unique()
    count = []
    for i in uniques:
        count.append(value.count(i))
    if len(uniques) == 2 and sorted(count) == [1,4]:
        return True
    else:
        return False

def full_house(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    new_value = pd.Series(value)
    uniques = new_value.unique()
    count = []
    for i in uniques:
        count.append(value.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else:
        return False

def flush(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    if color.count(color[0]) == 5:
        return True
    else:
        return False

def straight(draw):
    value, couleur = new_hand(draw)
    value = card_design(value)
    value = sorted(value)
    straight = []
    for e, i in zip(value[0:-1], range(len(value)-1)):
        if e+1 == value[i+1]:
            straight.append('True')
    if straight.count('true') == 4 or value == [1, 10, 11, 12, 13]:
        return True
    else:
        return False

def toak(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    new_value = pd.Series(value)
    uniques = new_value.unique()
    count = []
    for i in uniques:
        count.append(value.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False

def two_pair(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    new_value = pd.Series(value)
    uniques = new_value.unique()
    count = []
    for i in uniques:
        count.append(value.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
        return True
    else:
        return False

def one_pair(draw):
    value, color = new_hand(draw)
    value = card_design(value)
    new_value = pd.Series(value)
    uniques = new_value.unique()
    count = []
    for i in uniques:
        count.append(value.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        return False

def check_profit(second_draw, bet):
    if royal_flush(second_draw) == True:
        is_winner = True
        profit = bet*250
        result = R_FLUSH + str(profit)
        return is_winner, profit, result
    elif straight_flush(second_draw) == True:
        is_winner = True
        profit = bet*50
        result = STRAIGHT_FLUSH + str(profit)
        return is_winner, profit, result
    elif foak(second_draw) == True:
        is_winner = True
        profit = bet*25
        result = FOAK + str(profit)
        return is_winner, profit, result
    elif full_house(second_draw) == True:
        is_winner = True
        profit = bet*9
        result = FULL_HOUSE + str(profit)
        return is_winner, profit, result
    elif flush(second_draw) == True:
        is_winner = True
        profit = bet*6
        result = FLUSH + str(profit)
        return is_winner, profit, result
    elif straight(second_draw) == True:
        is_winner = True
        profit = bet*4
        result = STRAIGHT + str(profit)
        return is_winner, profit, result
    elif toak(second_draw) == True:
        is_winner = True
        profit = bet*3
        result = TOAK + str(profit)
        return is_winner, profit, result
    elif two_pair(second_draw) == True:
        is_winner = True
        profit = bet*2
        result = TP + str(profit)
        return is_winner, profit, result
    elif one_pair(second_draw) == True:
        is_winner = True
        profit = bet*1
        result = OP
        return is_winner, profit, result
    else:
        is_winner = False
        profit = 0
        result = LOOSE
        return is_winner, profit, result