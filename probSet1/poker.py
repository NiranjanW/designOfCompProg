def poker(hands):
	return max(hands  , key=hand_rank )


def hand_rank(hand):
	"Return a value indicating the ranking of hand"

	ranks =card_rank(hand)

	if straight(ranks) and flush(hand):
		return (8,max(ranks))
	elif kind(4,ranks):
		return (7, )

def card_rank(hand):
	"Return a list of hands sorted  with higher order"
	ranks = ['--23456789TJQKA'.index(r) for r , s in hand]
	ranks.sort(reversed =True)
	return ranks


def test():
	"test cases for funtions in poker"

	sf ="6C 7C 8C 9C TC".split()
	fk ="9D 9H 9S 9C 7D".split()
	fh-"TD TC TH 7C 7D".split()
	assert poker([sf ,fk ,fh]) == sf
	assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
	assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf


