class Cipher:
    def __init__(self, key=None):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.key = "aaaaaaaaaa"
        self.shift = []

        if key:
            for letter in key:
                self.shift.append(self.alphabet.index(letter))
        

    def encode(self, text):
        if not self.shift:
            return text
        
        new_text = ""
        counter = 0
        for letter in text:
            if counter + 1 > len(self.shift):
                counter = 0
            position = self.alphabet.index(letter) + self.shift[counter]
            if position > len(self.alphabet) - 1:
                position %= 26
            new_text += self.alphabet[position]
            counter += 1
        return new_text

    def decode(self, text):
        if not self.shift:
            return text
        
        new_text = ""
        counter = 0
        for letter in text:
            if counter + 1 > len(self.shift):
                counter = 0
            position = self.alphabet.index(letter) - self.shift[counter]
            if position < 0:
                position %= 26
            new_text += self.alphabet[position]
            counter += 1
            print(position)
        return new_text


if __name__ == "__main__":
    # cipher = Cipher("iamapandabear")
    # print(cipher.encode("iamapandabear")) #qayaeaagaciai
    cipher1 = Cipher("abcdefghij")
    print(cipher1.encode("zzzzzzzzzz")) #zabcdefghi
    print(cipher1.decode("zabcdefghi")) #zzzzzzzzzz

    # cipher2 = Cipher()
    # print(cipher2.encode("zzzzzzzzzz")) #zzzzzzzzzz
    # cipher3 = Cipher("abc")
    # print(cipher3.shift)
    # print(cipher3.encode("iamapandabear")) #iboaqcnecbfcr
    