'''
THIS PSEUDO CODE ISN'T RELEVANT, AS THE CODE HAS BEEN REVISIONED
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




'''