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
    "health": 100,
    "armour": 50,
    "base_damage": 10,
    "xp": 0
}

def lookup_stats():
    input_box.get().upper()
    if input_box.get().upper() == "C":
        output_box.insert("end", f"{player_stats}")
    else:
        pass

def main():
    output_box.insert("end", "Start Game? (Y/N):\n\n")
    input_box.bind("<Return>", start_game)

def start_game(event):
    text_input = input_box.get().upper()
    output_box.insert("end", f"You: {text_input}\n")
    input_box.delete(0, "end")

    while True:
        if text_input == "Y":
            output_box.after(1500)
            output_box.insert("end", Prologue1)
            output_box.after(1500)
            output_box.insert("end", Prologue2)
            output_box.after(1500)
            output_box.insert("end", Prologue3 + "\n")
            output_box.after(1500)
            output_box.insert("end", "What is your name, hero?\n\n")
            input_box.bind("<Return>", character_creation)
            break
        elif text_input == "N":
            output_box.insert("end", "Have a nice day, then.")
            break
        else:
            output_box.insert("end", "Come on, it's not a tough question.\n\n")
            main()
            break

def character_creation(event):
    player_name = input_box.get()
    output_box.insert("end", f"You: {player_name}\n\n")
    input_box.delete(0, "end")
    welcome(player_name)

def welcome(player_name):
    output_box.insert("end", f"Welcome, brave {player_name}.\n\n")
    output_box.after(1500)
    output_box.insert("end", "Will you answer the call to adventure? (Y/N):\n\n")
    input_box.unbind("<Return>")
    input_box.bind("<Return>", lambda event, name=player_name: heed_the_call(event, name))

def heed_the_call(event, player_name):
    heed_the_call = input_box.get().upper()
    output_box.insert("end", f"You: {heed_the_call}\n\n")
    input_box.delete(0, "end")

    if heed_the_call == "Y":
        output_box.insert("end", f"May the sun ever light your path, {player_name}.\n\n")

    elif heed_the_call == "N":
        output_box.insert("end", "And behold: the land fell into the abyss.\n\n")
        output_box.after(1500)
        output_box.insert("end", "The End.")
    else:
        output_box.insert("end", "Come on, it's not a tough question.\n\n")
        welcome(player_name)



window = tk.Tk()
window.title("Before The Flood")

output_box = scrolledtext.ScrolledText(master=window, wrap="word", height=30, width=90)
output_box.pack(fill="both", expand=True)

input_box = ttk.Entry(master=window, width=90)
input_box.pack(fill="x", padx=30)


main()
lookup_stats()

window.mainloop()