#this file will be used to check for valuable combinations of cards
from cards import available_cards



def count_ranks():
    '''This function put a counter next to all different ranks found in the available cards'''
    current_cards = available_cards()
    cardcounter={}
    #Add cards to dict, if card already exists in dict add 1 to the value
    for card in current_cards:
        if card[0] in cardcounter:
            cardcounter[card[0]]+=1
        else:
            cardcounter[card[0]]=1
    return cardcounter


def check_duplicates():
    '''This function will check for duplicates in counted ranks
    This includes: 2 of a kind, 3 of a kind, 4 of a kind & Full house
    The function will only return the rank and the amount of duplicates there are in the available cards,
    If there is no dupes, return none'''
    cardcounter = count_ranks()
    duplicates={}
    for key,value in cardcounter.items():
        if value>1:
            duplicates[key]=value
    if len(duplicates)>0:
        return duplicates
    else:
        return None

def sort_cards():
    ''' This function will take  the count_ranks dict, and return it sorted '''
    cr = count_ranks()
    sorted_cards = dict(sorted(cr.items()))
    return sorted_cards

def check_straight():
    '''This function will determine if there is a straight
    This function will return the 5 cards from the straight. If there is no straight : None
    it will do this by looping through the sorted cards, and adding 1 to a counter every time a card fits into a straight
    if this counter becomes 5, there is a straight
    for instance: loop through cards :  2,3,4,7,8,11,14
    start at 2, add 1 to counter
    go next, which is 3, which fits into a straight with the previous card, add 1 to counter, counter is now 2
    go next, which is 4, which fits into a straight with the previous card, add 1 to counter, counter is now 3
    go next, which is 7, which DOESNT fit into a straight with the previous cards, reset counter to 1
    go next, which is 8, which fits into a straight with the previous card, add 1 to counterm, counter is now 2
    go next, which is 11, which DOESNT fit into a straight with the previous cards, reset counter to 1'''

    sc = sort_cards()
    cards_ranksonly=list(sc) #cards_ranksonly is a list with only the unique ranks found in the available cards
    straight_counter=0  # counter explained in docstring in check_straight

    for i in range(len(cards_ranksonly)):
        if straight_counter==0:
            straight_counter+=1
            print(f'{straight_counter} cards in a row, with card {cards_ranksonly[i]}')
            continue
        if cards_ranksonly[i-1]+1==cards_ranksonly[i]:
            straight_counter += 1
        else:
            straight_counter = 1
        if straight_counter>=5:
            print(f'{straight_counter} cards in a row, with card {cards_ranksonly[i]}')
            print('STRAIGHT DETECTED')
            return [cards_ranksonly[i-4],cards_ranksonly[i-3],cards_ranksonly[i-2],cards_ranksonly[i-1],cards_ranksonly[i]]
        print(f'{straight_counter} cards in a row, with card {cards_ranksonly[i]}')




def count_suits():
    '''This function put a counter next to all different suits found in the available cards'''
    current_cards = available_cards()
    cardcounter={}
    #Add suit to dict, if suit already exists in dict add 1 to the value
    for card in current_cards:
        if card[1] in cardcounter:
            cardcounter[card[1]]+=1
        else:
            cardcounter[card[1]]=1
    return cardcounter

def check_flush():
    '''This function will check for duplicates in counted suits
    This function will return the suit of which there are 5 or more in the available cards
    If there is no dupes, return none'''
    cardcounter = count_suits()
    duplicates={}
    for key,value in cardcounter.items():
        if value>=5:
            duplicates[key]=value
    if len(duplicates)>0:
        return duplicates

    else:
        return None
i=0
while True:
    i += 1
    print(i)
    kijkdan = check_flush()
    if kijkdan !=None:
        print(kijkdan)

        
        print("kaas")


        quit()