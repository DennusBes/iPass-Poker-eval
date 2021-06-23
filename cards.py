import random

def gen_cards():
    '''
deck is a List containing all cards
All cards are lists, containing 2 numbers:
Card[0] will be the rank, and card[1]: Will be the suit
Rank will be 2 to 14, corresponding to the real ranks:2,3,4,5,6,7,8,9,10,J,Q,K,A
Suit will be 1 to 4,  corresponding with real suits: Clubs, diamonds, Hearts, spades'''
    deck = []
    for rank in range(2, 15, 1):
        for suit in range(1, 5, 1):
            card = [rank, suit]
            deck.append(card)
    return deck

def deal_cards():
    '''Deal random cards from the deck, and remove the cards that have been dealt from the remaining deck
    return hand,flop,turn,river and remaining deck '''
    dealdeck=gen_cards()
    if len(dealdeck)==52:
        hand = random.sample(dealdeck,2)
        dealdeck.remove(hand[0])
        dealdeck.remove(hand[1])
        flop = random.sample(dealdeck,3)
        dealdeck.remove(flop[0])
        dealdeck.remove(flop[1])
        dealdeck.remove(flop[2])
        turn = random.sample(dealdeck,1)
        dealdeck.remove(turn[0])
        river = random.sample(dealdeck, 1)
        dealdeck.remove(river[0])
    return hand,flop,turn,river,dealdeck

def available_cards():
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #turn = 2 is a temporary way getting more cards into available hand
    turns =2
    total_cards=deal_cards()
    #index 0 and 1 are hand and flop respectively
    available_cards=total_cards[0]+total_cards[1]

    if turns  > 0:  # add river bijvoorbeeld, turn maak ik aan in de simulatie van de stappen ergens
        available_cards+=total_cards[2]   #turn
        available_cards+=total_cards[3]   #river
    return  available_cards





