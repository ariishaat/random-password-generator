#Random password generator

import random
import secrets
import string as str

## global variables:
letters = str.ascii_letters
digits = str.digits
specialChars = str.punctuation

fullChars = letters + digits + specialChars
noSpecial = letters + digits

def randomPass(n, special):
    '''
    randomPass(n, special) generates a secured random password with 
    special characters if special = true, without special characters if false

    randomPass: Int Bool -> Str
    '''
    newPass = ""
    if n <= 7:
        return "Password is too short, please try again"
    elif special == True:
        ## for passwords with no constraints
        for i in range(n):
            newPass += "".join(secrets.choice(fullChars))
        return newPass
    elif special == False:
        ## for passwords when special chars can't be used, passwords 
        ## contain digits ∩ letters
        while not(any (char.isdigit() for char in newPass) and 
                  any(char.isalpha() for char in newPass)):
            for i in range(n):
                newPass += "".join(secrets.choice(noSpecial))
            return newPass
    else:
        return "Password cannot be generated"
    

# with User input:
def isSpecial():
    '''
    noPuncs() takes user input and converts input to Boolean

    noPuncs: None -> Bool
    '''
    while True:
        special = input("Special characters accepted? (y or n): ")
        if special == "y":
            return True
        elif special == "n":
            return False
        else:
            print("Please enter 'Yes' or 'No'.")

def generatePass():
    '''
    Takes user's input to generate a random password

    '''
    n = int(input("Enter password length: "))
    password = randomPass(n, isSpecial())
    print(password)


generatePass()