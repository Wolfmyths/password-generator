import random
import requests
import string
import urllib3 # Added so py installer could find the correct modules
class password:
    def __init__(self, symbols: bool = True, length: int = 0, capital: bool = True) -> None:
        self.symbolsBool = symbols
        self.length = length
        self.capitalBool = capital
        self.lowerCase = tuple(string.ascii_lowercase)
        self.upperCase = tuple(string.ascii_uppercase)
        self.symbols = tuple(string.punctuation)
        self.number = tuple(string.digits)
        self.charChoice = [self.lowerCase, self.number]

        if self.symbolsBool:
            self.charChoice.append(self.symbols)
        if self.capitalBool:
            self.charChoice.append(self.upperCase)

            
    def get_pass(self) -> str:
        password = ''

        length = int(self.length)
        if length <= 0:
            length = random.randint(1, 250)
        if length > 250:
            return f'The length "{length}" is too high, use 250 or below'

        for i in range(length):

            charChoice = random.choice(self.charChoice)
            i = random.choice(charChoice)
            
            password += i

        return password

    
class passphrase:
    def __init__(self, length: int = 0, capitalize: bool = True, allcaps: bool = False) -> None:
        self.length = length
        self.capitalize = capitalize
        self.allcaps = allcaps
    
    
    def get_phrase(self) -> str:
        password = ''

        length = int(self.length)
        if length <= 0:
            length = random.randint(1, 50)
        if length > 50:
            return f'The length "{length}" is too high, use 50 or below'
        
        try:
            word = requests.get(f'https://random-word-api.herokuapp.com/word?number={length}') # Access the random word API
        except requests.exceptions.Timeout:
            return 'Error: API connection timeout after 60 seconds.'
        except requests.exceptions.HTTPError:
            return 'Code 404 Error: Could not find API.'
        except:
            return 'Error: Something went wrong trying to connect to the API.'

        word = word.text
        word = word[1:-1]
        word = word.split(',') # Converts the output of the api into a list instead of it being a string
        for item in word:

            item = item[1:-1] # Each item in word has quotations around it ( "Example" ) , this line removes those

            if self.allcaps:
                item = item.upper()
            elif self.capitalize:
                item = item.title()

            if password == '': # If statement determines if the word being added to the passphrase is the first word
                password += item
            else:
                password += f' {item}'
        
        return password
