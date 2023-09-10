#Random 12 character password generator using tkinter
import random
import secrets
import string as str
import tkinter as tk

def randomPass():
    '''
    randomPass() generates a secured random password

    randomPass: None -> Str
    '''
    letters = str.ascii_letters
    digits = str.digits
    specialChars = str.punctuation

    fullChars = letters + digits + specialChars

    password_len = 12 
    password = ""
    
    for i in range(password_len):
            password += "".join(secrets.choice(fullChars))
    window_label.config(text=password)
    
    
window = tk.Tk()
window.title("Password Generator")
window.geometry("250x50")

generate_button = tk.Button(window, text="Generate Password", command=randomPass)
generate_button.pack()

window_label = tk.Label(window, text="")
window_label.pack()

window.mainloop()