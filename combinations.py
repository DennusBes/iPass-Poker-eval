#this file will be used to check for valuable combinations of cards
from cards import available_cards as ac

turn=0

global available_cards   #I'd like to not have a global variable, as I got told it's generally bad practice to use them. This is however currently not my focus in this project.
available_cards = ac(turn)[0]
global leftover_cards
leftover_cards = ac(turn)[1]


def count_ranks(available_cards):
    '''This function put a counter next to all different ranks found in the available cards'''
    cardcounter={} #Add cards to dict. if card already exists in dict, add 1 to the value instead
    for card in available_cards:
        if card[0] in cardcounter:
            cardcounter[card[0]]+=1
        else:
            cardcounter[card[0]]=1
    return cardcounter


def check_duplicates(available_cards):
    '''This function will check for duplicates in counted ranks
    This includes: 2 of a kind, 3 of a kind, 4 of a kind & Full house
    The function will only return the rank and the amount of duplicates there are in the available cards,
    If there is no dupes, return none'''
    cardcounter = count_ranks(available_cards)
    duplicates={}
    for key,value in cardcounter.items():
        if value>1:
            duplicates[key]=value
    if len(duplicates)>0:
        return duplicates
    else:
        return None

def sort_cards(available_cards):
    ''' This function will take  the count_ranks dict, and return it sorted '''
    cr = count_ranks(available_cards)
    sorted_cards = dict(sorted(cr.items()))
    return sorted_cards

def check_straight(available_cards):
    '''This function will determine if there is a straight
    This function will return the 5 cards from the straight. If there is no straight : None
    it will do this by looping through the sorted cards, and adding 1 to a counter every time a card fits into a straight
    if this counter becomes 5, there is a straight
    for instance: loop through cards :  2,3,4,7,8,J,A
    start at 2, add 1 to counter
    go next, which is 3, which fits into a straight with the previous card, add 1 to counter, counter is now 2
    go next, which is 4, which fits into a straight with the previous card, add 1 to counter, counter is now 3
    go next, which is 7, which DOESNT fit into a straight with the previous cards, reset counter to 1
    go next, which is 8, which fits into a straight with the previous card, add 1 to counterm, counter is now 2
    go next, which is J, which DOESNT fit into a straight with the previous cards, reset counter to 1'''

    sc = sort_cards(available_cards)
    cards_ranksonly=list(sc) #cards_ranksonly is a list with only the unique ranks found in the available cards
    straight_counter=0  # counter explained in docstring in check_straight

    for i in range(len(cards_ranksonly)):
        if straight_counter==0:
            straight_counter+=1
            continue
        if cards_ranksonly[i-1]+1==cards_ranksonly[i]:
            straight_counter += 1
        else:
            straight_counter = 1
        if straight_counter>=5:
            return [cards_ranksonly[i-4],cards_ranksonly[i-3],cards_ranksonly[i-2],cards_ranksonly[i-1],cards_ranksonly[i]]
    return None




def count_suits(available_cards):
    '''This function put a counter next to all different suits found in the available cards'''
    cardcounter={}
    #Add suit to dict, if suit already exists in dict add 1 to the value
    for card in available_cards:
        if card[1] in cardcounter:
            cardcounter[card[1]]+=1
        else:
            cardcounter[card[1]]=1
    return cardcounter

def check_flush(available_cards):
    '''This function will check for duplicates in counted suits
    This function will return the suit of which there are 5 or more in the available cards
    If there is no dupes, return none'''
    cardcounter = count_suits(available_cards)
    duplicates={}
    for key,value in cardcounter.items():
        if value>=5:
            duplicates[key]=value
    if len(duplicates)>0:
        return duplicates
    else:
        return None

def check_straightflush(available_cards):
    '''This function check for a straight flush in the available cards
    A straight flush, is a straight in which all cards have the same suit
    This function will return 5 cards if a straight flush has been found.
    If there is no straight flush, return none'''
    sf=[] # sf is a list which will keep track of which cards could be part of the straight flush
    straight_ranks = check_straight(available_cards)
    flush_suit = check_flush(available_cards)
    if check_flush(available_cards)== None or check_straight(available_cards)==None:  # If there is no flush, or no straight, there can't be a straightflush either
        return None
    for card in available_cards:
        if card[0] in straight_ranks:
            if card[1] in flush_suit:
                sf.append(card)
    if len(sf)==5:
        return sf
    else:
        return None

def check_turn(available_cards):
    '''This function checks what turn the game is on
    very ugly function'''
    turn=0
    if len(available_cards)==5:
        return  turn
    if len(available_cards)==6:
        turn=1
        return turn
    if len(available_cards)>6:
        turn=2
        return turn


def leftover_options(leftover_cards):
    '''This function creates all possible leftover options
    The amount of options is based on the turn, which is calculated in check_turns
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Currently this function adds redundant options. for instance : both [A,B] and [B,A] are added. this is bad and results in alot of useless options
    This won't affect the % odds, only the count.
    '''
    turns = check_turn(available_cards)
    if turn == 1:
        return leftover_cards
    if turn == 0:
        leftoverlist=[]
        for card1 in leftover_cards:
            for card2 in leftover_cards:
                if card1 !=card2:
                    leftoverlist.append([card1,card2])
        return leftoverlist
    if turn > 1:
        print("The game is over. No point in calculating more.")
        quit()

def calculate_odds(available_cards):
    ''' This function will loop through the available options, which are generated in leftover_options
    in this loop the options will get added to the current available cards and the results of check dupes etc will get counted
    in the end the results will get divided by the total amount of options, and then multiplied by 100. This will result in a %
    This % is the % of ALL options which will result in a wanted combination
    '''

    options=leftover_options(leftover_cards)

    defaultcards = available_cards
    print(defaultcards)
    pair,straight,flush,sf,tok,fh,fok,tp = 0,0,0,0,0,0,0,0  # tok= three of a kind,  fh= full house,  fok=  four of a kind   tp = two pair
    for option in options:
        temp_ac = defaultcards.copy()
        if check_turn(available_cards)==1:
            temp_ac.append(option)         #If only 1 card per option, just append
        else:
            for opt in option:             #If there's multiple cards to be added per option, use a loop
                temp_ac.append(opt)
        dupes = check_duplicates(temp_ac)
        if dupes!=None:
                if 3 in dupes.values() and 2 in dupes.values():
                    fh+=1
                if 4 in dupes.values():
                    fok+=1
                if 3 in dupes.values() :
                    tok+=1
                if 2 in dupes.values() :
                    pair+=1
        if check_straight(temp_ac) != None:
            straight+=1
        if check_flush(temp_ac) != None:
            flush+=1
        if check_straightflush(temp_ac) != None:
            sf+=1

    print(f'Pair:              {(pair/len(options))*100}%,\n'
          f'Three of a kind:   {(tok/len(options))*100}%,\n'
          f'Four of a kind:    {(fok/len(options))*100}%,\n'
          f'Full House:        {(fh/len(options))*100}%,\n'
          f'Straight           {(straight/len(options))*100}%,\n'
          f'Flush              {(flush/len(options))*100}%,\n'
          f'Straight flush     {(sf/len(options))*100}%')

calculate_odds(available_cards)
