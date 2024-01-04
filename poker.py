"""

S: spades
D: diamonds
C: clubes
H: hearts
A: aces
"""


def best_hands(hands: list[str]) -> list[str]:
    if len(hands) == 1:
        return hands

    winner = []
    hands_win = []

    # Straight flush
    for cards in hands:
        new_cards = cards.split()
        same_suit = []
        for card in new_cards:
            if len(new_cards[0]) == 3 and len(card) == 3:
                if card[2] == new_cards[0][2]:
                    # print("2", card[2], new_cards[0][2])
                    same_suit.append(card)
            elif len(new_cards[0]) == 3 and len(card) == 2:
                if card[1] == new_cards[0][2]:
                    # print("2", card[1], new_cards[0][2])
                    same_suit.append(card)
            elif len(new_cards[0]) == 2 and len(card) == 3:
                if card[2] == new_cards[0][1]:
                    # print("2", card[2], new_cards[0][1])
                    same_suit.append(card)
            elif card[1] == new_cards[0][1] and len(new_cards[0]) == 2:
                # print("1", card[1], new_cards[0])
                same_suit.append(card)

        # print(same_suit)
        if len(same_suit) == 5 and same_suit[2][0] != "A":
            hands_win.append(" ".join(new_cards))

    sum_score = []
    for cards in hands_win:
        if not hands_win:
            break
        score = []
        for value in cards:
            # print(cards)
            if value[0] == "1":
                score.append(10)
            elif value[0].isdigit() and value[0] != "0":
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(1)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        score.sort()
        if score[0] + 1 == score[1] and score[3] + 1 == score[4] or score[0] == 1 and score[3] + 1 == score[4]:
            sum_score.append(sum(score))
        # print("score ", score)
    # print(hands_win)
    if hands_win and sum_score:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Four of a kind
    hands_win = []
    for cards in hands:
        new_cards = cards.split()
        cards_ordered = sorted(new_cards)
        same_number = []
        for card in new_cards:
            # print(card[0], cards_ordered[2][0])
            if cards_ordered[2][0] == card[0] and len(card) == 2:
                same_number.append(card)
            if len(card) == 3:
                if card[:2] == cards_ordered[2][:2]:
                    same_number.append(card)

        # print(same_number)
        if len(same_number) == 4:
            hands_win.append(" ".join(new_cards))

    sum_score = []

    for cards in hands_win:
        if not hands_win:
            break
        score = []
        for value in cards:
            if value[0].isdigit():
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(1)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        sum_score.append(sum(score))
        # print("score ", sum_score)
    # print(winner)
    if hands_win:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Full house
    hands_win = []
    for cards in hands:
        new_cards = cards.split()
        cards_ordered = sorted(new_cards)
        cards_value = [card[0] for card in cards_ordered]
        value1 = cards_value.count(cards_value[0])
        value2 = cards_value.count(cards_value[3])
        # print("value 1", value1, "value2", value2, cards_ordered)
        same_number = []
        if value1 == 2 and value2 == 3 or value1 == 3 and value2 == 2:
            hands_win.append(" ".join(new_cards))

    sum_score = []

    for cards in hands_win:
        if not hands_win:
            break
        score = []
        for value in cards:
            if value[0].isdigit():
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(1)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        sum_score.append(sum(score))
        # print("score ", sum_score)
    # print(winner)
    if hands_win and hands_win:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Flush
    hands_win = []

    for cards in hands:
        new_cards = cards.split()

    sum_score = []
    for cards in hands_win:
        if not hands_win:
            break
        score = []
        for value in cards:
            print(cards)
            if value[0] == "1":
                score.append(10)
            elif value[0].isdigit() and value[0] != "0":
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(1)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        score.sort()
        sum_score.append(sum(score))
        print("score ", score)
    # print(hands_win)
    if hands_win and sum_score:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Straight
    hands_win = []
    # print(hands)

    sum_score = []
    # print(new_cards)

    for cards in hands:
        score = []
        for value in cards:
            if value[0] == "1":
                score.append(10)
            elif value[0].isdigit() and value[0] != "0":
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(1)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        # print(score)
        if score[2] == 1:
            continue
        score.sort()
        if score[0] + 1 == score[1] and score[3] + 1 == score[4] or score[0] == 1 and score[3] + 1 == score[4] or score[0] + 1 == score[1] and score[4] == 1:
            sum_score.append(sum(score))
            hands_win.append(cards)
        # print(sum_score)

    # print(hands_win)
    if hands_win and sum_score:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Three of a kind
    hands_win = []
    for cards in hands:
        new_cards = cards.split()
        cards_ordered = sorted(new_cards)
        cards_value = [card[0] for card in cards_ordered]
        value1 = cards_value.count(cards_value[0])
        value2 = cards_value.count(cards_value[3])
        # print("value 1", value1, "value2", value2, cards_ordered)
        same_number = []
        if value2 == 3 or value1 == 3:
            hands_win.append(" ".join(new_cards))

    sum_score = []

    for cards in hands_win:
        if not hands_win:
            break
        score = []
        for value in cards:
            if value[0] == "1":
                score.append(10)
            elif value[0].isdigit() and value[0] != "0":
                score.append(int(value[0]))
            elif value[0] == "A":
                score.append(10)
            elif value[0] == "K":
                score.append(13)
            elif value[0] == "Q":
                score.append(12)
            elif value[0] == "J":
                score.append(11)
        sum_score.append(sum(score))
        # print("score ", sum_score)
    # print(winner)
    if hands_win and hands_win:
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # Two pair
    hands_win = []
    pair_one = []
    pair_two = []
    for cards in hands:
        new_cards = cards.split()
        cards_ordered = sorted(new_cards)
        cards_value = [card[0] for card in cards_ordered]
        value1 = cards_value.count(cards_value[1])
        value2 = cards_value.count(cards_value[3])
        # print("value 1", value1, "value2", value2, cards_ordered)
        if value2 == 2 and value1 == 2:
            hands_win.append(" ".join(new_cards))
            if cards_value[1] == "J":
                pair_one.append(11 * 2)
            if cards_value[3] == "J":
                pair_two.append(11 * 2)
            if cards_value[1] == "Q":
                pair_one.append(12 * 2)
            if cards_value[3] == "Q":
                pair_two.append(12 * 2)
            if cards_value[1] == "K":
                pair_one.append(13 * 2)
            if cards_value[3] == "K":
                pair_two.append(13 * 2)
            if cards_value[1].isdigit():
                pair_one.append(int(cards_value[1]) * 2)
            if cards_value[3].isdigit():
                pair_two.append(int(cards_value[3]) * 2)

    sum_score = []

    for index, cards in enumerate(hands_win):
        if not hands_win:
            break
        score = []
        score.append(pair_one[index] + pair_two[index])
        sum_score.append(sum(score))
        # print("score ", sum_score)
    # print(winner)
    if hands_win and hands_win:
        if len(sum_score) > 1 and sum_score[0] == sum_score[1]:
            if pair_one[pair_one.index(max(pair_one))] > pair_two[pair_two.index(max(pair_two))]:
                winner.append(hands_win[0])
                return winner
            if pair_one[pair_one.index(max(pair_one))] < pair_two[pair_two.index(max(pair_two))]:
                winner.append(hands_win[1])
                return winner
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner

    # One pair
    hands_win = []
    pair_one = []
    pair_two = []
    for cards in hands:
        new_cards = cards.split()
        cards_ordered = sorted(new_cards)
        cards_value = [card[0] for card in cards_ordered]
        value1 = cards_value.count(cards_value[1])
        value2 = cards_value.count(cards_value[3])
        # print("value 1", value1, "value2", value2, cards_ordered)
        if value2 == 2 or value1 == 2:
            hands_win.append(" ".join(new_cards))
            if cards_value[1] == "J":
                pair_one.append(11 * 2)
            if cards_value[3] == "J":
                pair_two.append(11 * 2)
            if cards_value[1] == "Q":
                pair_one.append(12 * 2)
            if cards_value[3] == "Q":
                pair_two.append(12 * 2)
            if cards_value[1] == "K":
                pair_one.append(13 * 2)
            if cards_value[3] == "K":
                pair_two.append(13 * 2)
            if cards_value[1].isdigit():
                pair_one.append(int(cards_value[1]) * 2)
            if cards_value[3].isdigit():
                pair_two.append(int(cards_value[3]) * 2)

    sum_score = []

    for index, cards in enumerate(hands_win):
        if not hands_win:
            break
        score = []
        score.append(pair_one[index] + pair_two[index])
        sum_score.append(sum(score))
        # print("score ", sum_score)
    # print(winner)
    if hands_win and hands_win:
        if len(sum_score) > 1 and sum_score[0] == sum_score[1]:
            if pair_one[pair_one.index(max(pair_one))] > pair_two[pair_two.index(max(pair_two))]:
                winner.append(hands_win[0])
                return winner
            if pair_one[pair_one.index(max(pair_one))] < pair_two[pair_two.index(max(pair_two))]:
                winner.append(hands_win[1])
                return winner
        winner.append(hands_win[sum_score.index(max(sum_score))])
        return winner



if __name__ == "__main__":
    # print(best_hands(["4S 5S 7H 8D JC"]))

    # Straight flush
    # print(best_hands(["2H 3H 4H 5H 6H", "4D AD 3D 2D 5D"])) #["2H 3H 4H 5H 6H"]
    # print(best_hands(["2C AC QC 10C KC", "QH KH AH 2H 3H"])) #["2C AC QC 10C KC"]
    # print(best_hands(["KC AH AS AD AC", "10C JC QC KC AC"])) #["10C JC QC KC AC"]

    # Four of a kind
    # print(best_hands(["2S 2H 2C 8D 2D", "4S 5H 5S 5D 5C"])) #["4S 5H 5S 5D 5C"]
    # print(best_hands(["4S 5H 4D 5D 4H", "3S 3H 2S 3D 3C"])) #["3S 3H 2S 3D 3C"]

    # Full house
    # print(best_hands(["3H 6H 7H 8H 5H", "4S 5H 4C 5D 4H"])) #["4S 5H 4C 5D 4H"]
    # print(best_hands(["4H 4S 4D 9S 9D", "5H 5S 5D 8S 8D"])) #["5H 5S 5D 8S 8D"]
    # print(best_hands(["5H 5S 5D 9S 9D", "5H 5S 5D 8S 8D"])) #["5H 5S 5D 9S 9D"]

    # Flush
    # print(best_hands(["4C 6H 7D 8D 5H", "2S 4S 5S 6S 7S"])) #["2S 4S 5S 6S 7S"]
    # print(best_hands(["4H 7H 8H 9H 6H", "2S 4S 5S 6S 7S"])) #["4H 7H 8H 9H 6H"]

    # Straight
    # print(best_hands(["4S 5H 4C 8D 4H", "3S 4D 2S 6D 5C"])) #["3S 4D 2S 6D 5C"]
    # print(best_hands(["4S 5H 4C 8D 4H", "10D JH QS KD AC"])) #["10D JH QS KD AC"]
    # print(best_hands(["4S 5H 4C 8D 4H", "4D AH 3S 2D 5C"])) #["4D AH 3S 2D 5C"]
    # print(best_hands(["2C 3D 7H 5H 2S", "QS KH AC 2D 3S"])) #["2C 3D 7H 5H 2S"]
    # print(best_hands(["4S 6C 7S 8D 5H", "5S 7H 8S 9D 6H"])) #["5S 7H 8S 9D 6H"]
    # print(best_hands(["2H 3C 4D 5D 6H", "4S AH 3S 2D 5H"])) #["2H 3C 4D 5D 6H"]

    # Three of a kind
    # print(best_hands(["2S 8H 2H 8D JH", "4S 5H 4C 8S 4H"])) #["4S 5H 4C 8S 4H"]
    # print(best_hands(["2S 2H 2C 8D JH", "4S AH AS 8C AD"])) #["4S AH AS 8C AD"]
    # print(best_hands(["4S AH AS 7C AD", "4S AH AS 8C AD"])) #["4S AH AS 8C AD"]

    # Two pair
    # print(best_hands(["2S 8H 6S 8D JH", "4S 5H 4C 8C 5C"])) #["4S 5H 4C 8C 5C"]
    # print(best_hands(["2S 8H 2D 8D 3H", "4S 5H 4C 8S 5D"])) #["2S 8H 2D 8D 3H"]
    # print(best_hands(["6S 6H 3S 3H AS", "7H 7S 2H 2S AC"])) #["7H 7S 2H 2S AC"]
    # print(best_hands(["2S QS 2C QD JH", "JD QH JS 8D QC"])) #["JD QH JS 8D QC"]
    # ["6S 2S 6H 7C 2C"]
    # print(best_hands(["5C 2S 5S 4H 4C", "6S 2S 6H 7C 2C"]))
    
    # One pair
    print(best_hands(["4S 5H 6C 8D KH", "2S 4H 6S 4D JH"])) #["2S 4H 6S 4D JH"]
    print(best_hands(["4S 2H 6S 2D JH", "2S 4H 6C 4D JD"])) #["2S 4H 6C 4D JD"]
    print(best_hands(["JD QH JS 8D QC", "JS QS JC 2D QD"])) #["JD QH JS 8D QC"]
    print(best_hands(["5C 2S 5S 4H 4C", "6S 2S 6H 7C 2C"])) #["6S 2S 6H 7C 2C"]



