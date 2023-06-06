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
def noPuncs():
    '''
    noPuncs() takes user input and converts input to Boolean

    noPuncs: None -> Bool
    '''
    special = input("Special characters accepted?: ")
    if special == "Yes":
        return True
    if special == "No":
        return False


n = int(input("Enter password length: "))
randomPass(n, noPuncs())