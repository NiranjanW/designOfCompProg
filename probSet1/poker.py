def poker(hands):
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Return a value indicating the ranking of hand"

    ranks = card_rank(hand)

    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))


def card_rank(hand):
    "Return a list of hands sorted  with higher order"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks


def kind(n, ranks):
    """ Return the first rank that this hand has exactly n of
    Return null if there is no n-of -a akind"""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def straight(rank):

    return (max(rank) - min(rank) == 4) and len(set(rank)) == 5
    # if len(rank) == len(set(rank)):
    #     return True
    # else:
    #     return False
    # set = ()
    # for v in rank:
    # 	if v in set: return False
    # 	s.add(v)
    # return True


def flush(hand):
    " return true is all cards have the same suit"

    suits = [s for r, s in hand]
    return len(suits) == 1


def test():
    "test cases for functions in poker"

    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    # assert flush(sf)
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
   # assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
   # assert poker([sf] + 99*[fh]) == sf


def main():
    test()


if __name__ == '__main__':

    main()
