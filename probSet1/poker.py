def poker(hands):
	return max(hands  , key=hand_rank )


def hand_rank(hand):
	"Return a value indicating the ranking of hand"

	ranks =card_rank(hand)

	if straight(ranks):
		return

def test():
	"test cases for funtions in poker"

	sf ="6C 7C 8C 9C TC".split()
	fk ="9D 9H 9S 9C 7D".split()
	fh-"TD TC TH 7C 7D".split()
	assert poker([sf ,fk ,fh]) == sf


