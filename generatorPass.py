import tkinter as tk
import random
import string

# create window
window = tk.Tk()
window.title('Generator Parole')

# determine screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# sets the dimensions and positioning of the window so that it is centered on the screen
window.geometry(f'500x300+{screen_width//2 - 250}+{screen_height//2 - 150}')

# Function for generating password
def generatePass(length, useUppercase, useLowercase, useNumbers, useSpecialCharacters):
    # Create a list of characters that can be included in the password
    characters = ""
    # uppercase
    if useUppercase:
        characters += string.ascii_uppercase
    # lowercase
    if useLowercase:
        characters += string.ascii_lowercase
    # numbers
    if useNumbers:
        characters += string.digits
    # special characters
    if useSpecialCharacters:
        characters += string.punctuation

    # Generate the password
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Function called when btnClick is pressed
def btnClick():
    # get values from the user input
    length = length_var.get()
    if length.isdigit():
        lengthPass = int(length)
        useUppercase = uppercase_var.get()
        useLowercase = lowercase_var.get()
        useNumbers = numbers_var.get()
        useSpecialCharacters = special_var.get()

        if useUppercase or useLowercase or useNumbers or useSpecialCharacters:
            # call the generatePass function with the user input values
            password = generatePass(lengthPass, useUppercase, useLowercase, useNumbers, useSpecialCharacters)
            # update the password label with the generated password
            password_label.config(text=password, fg="#0066cc")
            error_label.config(text="")
        else:
            password_label.config(text="")
            error_label.config(text="Error: Please check at least one character option.", fg="red")
    else:
        password_label.config(text="")
        error_label.config(text="Error: Please enter a valid number for the password length.", fg="red")

# variables for storing the user input
length_var = tk.StringVar()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# create the length label and entry
length_label = tk.Label(window, text="Password Length")
length_entry = tk.Entry(window, textvariable=length_var)

# create the checkboxes for character options
uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
lowercase_checkbox = tk.Checkbutton(window, text="Include Lowercase Letters", variable=lowercase_var)
numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
special_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=special_var)

# create the generate button and password label
generate_button = tk.Button(window, text="Generate Password", command=btnClick)
password_label = tk.Label(window, text="")
error_label = tk.Label(window, text="")

# place the widgets on the grid
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)
uppercase_checkbox.grid(row=1, column=0, columnspan=2)
lowercase_checkbox.grid(row=2, column=0, columnspan=2)
numbers_checkbox.grid(row=3, column=0, columnspan=2)
special_checkbox.grid(row=4, column=0, columnspan=2)
generate_button.grid(row=5, column=0, columnspan=2)
password_label.grid(row=6, column=0, columnspan=2)
error_label.grid(row=7, column=0, columnspan=2)

# run app
window.mainloop()