import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

Prologue1 = '''
This land has wasted its summer in decadence. Its people have lived too long under an open sky. 
The fields lie fallow and barren, the libraries lost to dust, and the barracks long since abandoned.
And in the distant east, a darkness is forming. Ebon clouds billow up from beyond the horizon. 
They cackle as lightning lashes out against the broiling sea. And somewhere, deep beneath the surface, an ancient evil awakens from its slumber.
'''

Prologue2 = '''
Who will save the land from the tempest? Who will fight that great serpent of old?
Only one will heed the call to pick up their sword, go forth to meet the tide, and stand... 
'''

Prologue3 = '''
Before The Flood.
'''

player_stats = {
    "Health": 100,
    "Armour": 50,
    "Base Damage": 10,
    "XP": 0
}

class GameState:
    MAIN_MENU = 0
    CHARACTER_CREATION = 1
    GAME_PLAYING = 2
    GAME_END = 3

current_state = GameState.MAIN_MENU

def main():
    output_box.insert("end", "Start Game? (Y/N):\n\n")
    input_box.bind("<Return>", start_game)

def start_game(event):
    global current_state
    text_input = input_box.get().upper()
    output_box.insert("end", f"You: {text_input}\n")
    input_box.delete(0, "end")

    if text_input == "Y":
        current_state = GameState.GAME_PLAYING
        display_prologue()
    elif text_input == "N":
        current_state = GameState.GAME_END
        output_box.insert("end", "Have a nice day, then.\n\n")
    else:
        output_box.insert("end", "Come on, it's not a tough question.\n\n")
        main()

def display_prologue():
    global current_state
    output_box.after(1500)
    output_box.insert("end", Prologue1)
    output_box.after(1500)
    output_box.insert("end", Prologue2)
    output_box.after(1500)
    output_box.insert("end", Prologue3 + "\n")
    output_box.after(1500)
    output_box.insert("end", "What is your name, hero?\n\n")
    current_state = GameState.CHARACTER_CREATION
    input_box.bind("<Return>", character_creation)

def character_creation(event):
    global current_state
    player_name = input_box.get()
    output_box.insert("end", f"You: {player_name}\n\n")
    input_box.delete(0, "end")
    welcome(player_name)
    current_state = GameState.GAME_PLAYING

def welcome(player_name):
    global current_state
    output_box.insert("end", f"Welcome, brave {player_name}.\n\n")
    output_box.after(1500)
    output_box.insert("end", "Will you answer the call to adventure? (Y/N):\n\n")
    input_box.unbind("<Return>")
    input_box.bind("<Return>", heed_the_call)

def heed_the_call(event):
    global current_state
    heed_the_call = input_box.get().upper()
    output_box.insert("end", f"You: {heed_the_call}\n\n")
    input_box.delete(0, "end")

    if heed_the_call == "Y":
        output_box.insert("end", "May the sun ever light your path.\n\n")
    elif heed_the_call == "N":
        output_box.insert("end", "And behold: the land fell into the abyss.\n\n")
        output_box.after(1500)
        output_box.insert("end", "The End.\n")
    else:
        output_box.insert("end", "Come on, it's not a tough question.\n\n")
        welcome(player_name)

# Define other functions as needed

# Tkinter setup
window = tk.Tk()
window.title("Before The Flood")

output_box = scrolledtext.ScrolledText(master=window, wrap="word", height=30, width=90)
output_box.pack(fill="both", expand=True)

input_box = ttk.Entry(master=window, width=90)
input_box.pack(fill="x", padx=30)

# Start the game
main()

# Start the Tkinter event loop
window.mainloop()
