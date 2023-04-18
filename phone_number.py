import re

class PhoneNumber:
    def __init__(self, number):
        restrictions = re.compile("[a-z]")
        
        if restrictions.search(number) != None:
        # if a phone number has letters in place of some digits.
            raise ValueError("letters not permitted")

        restrictions = re.compile("[@:!#$%&/]")
        if restrictions.search(number) != None:
            # if a phone number has punctuation in place of some digits.
            raise ValueError("punctuations not permitted")
        
        self.number_phone = re.split("[\W]", number)
        numero = []
        digits_phone = 0
        
        
        if len(self.number_phone) == 1 and self.number_phone[0].startswith("1"):
            self.number_phone = self.number_phone[0][1:]
        
        
        if len(number) == 10:
            self.number_phone = []
            for i in range(3):
                if i == 0:
                    self.number_phone.append(number[:3])
                if i == 1:
                    self.number_phone.append(number[3:6])
                if i == 2:
                    self.number_phone.append(number[6:])
        
        print("number_phone ", self.number_phone)
        
        
        
        for i in self.number_phone:
            if i == '':
                continue
            numero.append(i)
            digits_phone += len(i)


        self.number = ''
        for i in self.number_phone:
            if i == '' or i == '1':
                continue
            self.number += i

        self.area_code = self.number[:3]
            
        # if a phone number has less than 10 digits.
        if digits_phone < 10:
            raise ValueError("incorrect number of digits")
            
        
        # if a phone number has more than 11 digits.
        if digits_phone > 11:
            raise ValueError("more than 11 digits")
            
        
        # if a phone number has 11 digits, but starts with a number other than 1.
        if digits_phone >= 11 and numero[0] != '1':
            raise ValueError("11 digits must start with 1")
        
        
        # if a phone number has an exchange code that starts with 0.
        if numero[-2].startswith('0'):
            raise ValueError("exchange code cannot start with zero")
            
        # if a phone number has an exchange code that starts with 1.
        if numero[-2].startswith('1'):
            raise ValueError("exchange code cannot start with one")

            
        # if a phone number has an area code that starts with 0.
        if numero[-3].startswith('0'):
            raise ValueError("area code cannot start with zero")
        
        
        # if a phone number has an area code that starts with 1.
        if numero[-3].startswith('1'):
            raise ValueError("area code cannot start with one")
    
    def pretty(self):
        number_pretty = ""
        for index, value in enumerate(self.number):
            if index == 0:
                number_pretty += "("
            if index == 3:
                number_pretty += ")-"
            if index == 6:
                number_pretty += "-"
            number_pretty += value
        return number_pretty

number = PhoneNumber("2234567890")
print(number.area_code)