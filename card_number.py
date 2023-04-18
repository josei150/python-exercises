import re

class Luhn:
    def __init__(self, card_num):
        self.input_card_number = card_num
        card = re.split("[\D]", card_num)
        self.card_num = []
        card_reversed = []
        self.valid_card = True
        
        for i in card:
            if i == "":
                continue
            for j in i:
                card_reversed.append(int(j))

        for index, j in enumerate(reversed(card_reversed)):
            if index == 0:
                self.card_num.append(int(j))
            elif index % 2 != 0:
                if int(j) * 2 > 9:
                    self.card_num.append(int(j) * 2 - 9)
                else:
                    self.card_num.append(int(j) * 2)
            else:
                self.card_num.append(int(j))

        
        print(self.card_num)

    def valid(self):

        if re.search("[@:!#$%&/-]", self.input_card_number) or re.search("[a-z]", self.input_card_number):
            return False

        if sum(self.card_num) % 10 != 0:
            return False

        if len(self.card_num) <= 1:
            return False

        print(sum(self.card_num))
        return self.valid_card

if __name__ == "__main__":
    card = Luhn("055-444-285")
    print(card.valid())