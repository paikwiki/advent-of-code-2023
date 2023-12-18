def split_n_strip(line: str, sep: str):
    splits = [ln.strip() for ln in line.split(sep)]
    return list(filter(lambda line: line, splits))


def solve1(lines: str):
    line_items_list = [split_n_strip(line, " ") for line in split_n_strip(lines, "\n")]
    cards_n_bet = [(cards, int(bet)) for [cards, bet] in line_items_list]

    five_of_a_kinds = []
    four_of_a_kinds = []
    full_houses = []
    three_of_a_kinds = []
    two_pairs = []
    one_pairs = []
    high_cards = []

    four_of_a_kindables = []
    three_of_a_kindables = []
    for cards, bet in cards_n_bet:
        card_set = set(cards)

        if len(card_set) == 1:
            five_of_a_kinds.append((cards, bet))
        elif len(card_set) == 2:
            four_of_a_kindables.append((cards, bet))
        elif len(card_set) == 3:
            three_of_a_kindables.append((cards, bet))
        elif len(card_set) == 4:
            one_pairs.append((cards, bet))
        else:
            high_cards.append((cards, bet))

    def count_each(cards: str):
        counts = {}
        for card in cards:
            if card in counts:
                counts[card] += 1
            else:
                counts[card] = 1
        return counts

    for cards, bet in four_of_a_kindables:
        counts = count_each(cards)

        if 4 in counts.values():
            four_of_a_kinds.append((cards, bet))
        else:
            full_houses.append((cards, bet))

    for cards, bet in three_of_a_kindables:
        counts = count_each(cards)
        if 3 in counts.values():
            three_of_a_kinds.append((cards, bet))
        else:
            two_pairs.append((cards, bet))

    CHAR_RANKS = {
        "A": 1,
        "K": 2,
        "Q": 3,
        "J": 4,
        "T": 5,
        "9": 6,
        "8": 7,
        "7": 8,
        "6": 9,
        "5": 10,
        "4": 11,
        "3": 12,
        "2": 13,
    }

    def cond(pos: int):
        def _cond(cards_n_bet):
            return CHAR_RANKS[cards_n_bet[0][pos]]

        return _cond

    for pos in [4, 3, 2, 1, 0]:
        five_of_a_kinds = sorted(five_of_a_kinds, key=cond(pos))
        four_of_a_kinds = sorted(four_of_a_kinds, key=cond(pos))
        full_houses = sorted(full_houses, key=cond(pos))
        three_of_a_kinds = sorted(three_of_a_kinds, key=cond(pos))
        two_pairs = sorted(two_pairs, key=cond(pos))
        one_pairs = sorted(one_pairs, key=cond(pos))
        high_cards = sorted(high_cards, key=cond(pos))

    all = (
        five_of_a_kinds
        + four_of_a_kinds
        + full_houses
        + three_of_a_kinds
        + two_pairs
        + one_pairs
        + high_cards
    )
    rank_point = len(all)

    point = 0
    for cards, bet in all:
        point = point + (bet * rank_point)
        rank_point -= 1

    return point


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
