'''
THIS PSEUDO CODE ISN'T ACCURATE, BECAUSE THE CODE HAS BEEN RESTRUCTURED
I've left this in for the sake of transparency
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


found combinations =[]    I save he found combo's .This makes it easier to identify a full house ( pair + three of a kind ),
totalscore =0
available cards = cards in hand + flop

-----------------------------------------------PAIRS--------------------------------------------
I check for pair in different places, because a pair that is in the flop, shouldnt give the hand more points, because all other players have that aswell
These will also check for three ,four and five of a kind
These for loops are ugly I need to think of something else
Will save something like [Pair, Rank, Amount] meaning three of a kind Aces would look like [ pair, 14, 3]


for cards in range len flop:
    if cards contain pair:
        score doesnt go up,
        combinations.append combination that has been found


for cards in range len hand:
    if cards contain pair :
        score goes up, (score height depends on what card was a pair)
        combinations.append combination that has been found

for cardsF in flop
    for cardsH in hand
        if cardsH[0] == cardsF[0]:
            score goes up, (score height depends on what card was a pair)
            combinations.append combination that has been found

-----------------------------------------------straight flush--------------------------------------------
function to check if there is a straight flush.
This function will make it very easy to check for a royal flush.
straight flush will return the 5 cards that make up the straight flush in an ordered manner.
If the last card is an Ace, there is a royal flush

check for striaght flush:
check if there is even a straight\
    lets say there is a straight, 2,3,4,5,6
Loop through all cards ( the cards are sorted already ):


    if card rank not in straight:
        continue
    if card rank in straight
        if cardrank is straight[0]
            2 Aces is in straight, so append to a flushlist,
            there is a 2 Hearts (different suit) append that to the flushlist aswell

        now onto the '3'. Let's say there's two 3's available.
        for checkcard in flushlist
            if card[1] ==checkcard[1]

WHAT IF i could use checkflush function to decide what rank even has a possibilty to get a flush at all

for card in all_cards:
    if card rank not in straight:
        continue





'''