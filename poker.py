from collections import Counter


RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def is_flush(cards):

    suits = [card[1] for card in cards]

    return len(set(suits)) == 1


def is_straight(cards):

    values = sorted(
        [RANK_VALUES[card[0]] for card in cards]
    )

    for i in range(4):

        if values[i] + 1 != values[i + 1]:
            return False

    return True


def evaluate(cards):

    ranks = [card[0] for card in cards]

    values = sorted(
        [RANK_VALUES[r] for r in ranks],
        reverse=True
    )

    counts = Counter(ranks)

    occurrences = sorted(
        counts.values(),
        reverse=True
    )

    flush = is_flush(cards)

    straight = is_straight(cards)

    # Royal Flush
    if flush and sorted(values) == [10, 11, 12, 13, 14]:
        return (10, "Royal Flush")

    # Straight Flush
    if flush and straight:
        return (9, "Straight Flush")

    # Four Of A Kind
    if occurrences == [4, 1]:
        return (8, "Four Of A Kind")

    # Full House
    if occurrences == [3, 2]:
        return (7, "Full House")

    # Flush
    if flush:
        return (6, "Flush")

    # Straight
    if straight:
        return (5, "Straight")

    # Three Of A Kind
    if occurrences == [3, 1, 1]:
        return (4, "Three Of A Kind")

    # Two Pair
    if occurrences == [2, 2, 1]:
        return (3, "Two Pair")

    # Pair
    if occurrences == [2, 1, 1, 1]:
        return (2, "Pair")

    return (1, "High Card")


def determine_winner(
        player_cards,
        bot1_cards,
        bot2_cards,
        bot3_cards):

    player_score = evaluate(player_cards)

    bot1_score = evaluate(bot1_cards)

    bot2_score = evaluate(bot2_cards)

    bot3_score = evaluate(bot3_cards)

    results = {

        "player": player_score,

        "bot1": bot1_score,

        "bot2": bot2_score,

        "bot3": bot3_score

    }

    winner = max(
        results,
        key=lambda x: results[x][0]
    )

    return winner, results