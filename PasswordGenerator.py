import random
import requests
class password:
    def __init__(self, strength='strong', length=0, capital='true'):
        self.strength = strength
        self.length = length
        self.capital = capital
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.symbols = ['!', '@', '#', '$', '&', '_']
        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
        self.charChoice = [self.alphabet, self.number, self.symbols]

    def get_pass(self):
        password = ''

        length = int(self.length)
        if length <= 0:
            length = random.randint(1, 250)
        if length > 250:
            return f'The length "{length}" is too high, use 250 or below'

        for i in range(length):

            charChoice = self.charChoice[random.randint(0, 2)] if self.strength == 'strong' else self.charChoice[random.randint(0, 1)] #If the strength is set to strong it will include the index value for symbols
            i = charChoice[random.randint(0, (len(charChoice) - 1))] # subtracts 1 from the list length to compensate lists in python being starting sub 0

            if self.capital == 'true' and i in self.alphabet: #If statement checks if the character can be capitalised
                if random.randint(0, 1) == 1: #Coin flip
                    i = i.upper()
            
            password += i

        return password

class passphrase:
    def __init__(self, length=0, capitalize='false'):
        self.length = length
        self.capitalize = capitalize
    
    def get_phrase(self):
        password = ''

        length = int(self.length)
        if length <= 0:
            length = random.randint(1, 50)
        if length > 250:
            return f'The length "{length}" is too high, use 250 or below'
        
        for i in range(length):
            word = requests.get('https://random-word-api.herokuapp.com/word')
            word = word.text
            word = word[2:-2]
            if self.capitalize == 'true':
                word.title()
            if password == '':
                password += word
            else:
                password += f' {word}'
        
        return password