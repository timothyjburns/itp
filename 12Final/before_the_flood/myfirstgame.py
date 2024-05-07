from gui import create_gui
from character_class import Character, Weapon, Hero, Leviathan, HealthBar, Rat
from game_class import Game
from pygame import mixer

window, output_box, input_box = create_gui()


Prologue1 = '''
This land has wasted its summer in decadence. Its people have lived too long under an open sky. 
The fields lie fallow and barren; the libraries lost to dust; the watchtowers long since abandoned.
'''

Prologue1_1 = '''
And in the distant east, a darkness is forming. Ebon clouds billow up from beyond the horizon. 
They cackle as lightning lashes out against the broiling sea. And somewhere, deep beneath the surface, an ancient evil awakens from its slumber.
'''

Prologue2 = '''
Who will save the land from the tempest? Who will fight that great serpent of old?
Only one will heed the call to pick up their sword, go forth to meet the tide, and stand... 
'''

Prologue3 = '''
Before The Flood
'''

def main():
    insert_and_scroll("Start Game? (Y/N):\n\n")
    input_box.bind("<Return>", start_game)


def wait():
    output_box.after(2000)

def insert_and_scroll(text, tag=None):
    output_box.insert("end", text, tag)
    output_box.see("end")

def handle_response(callback, event=None, player_name=None):
    response = input_box.get().upper()
    insert_and_scroll(f"You: {response}\n\n")
    input_box.delete(0, "end")
    callback(response.lower(), player_name)

def bold_text(text, bold_words):
    words = text.split(' ')
    for i, word in enumerate(words):
        if word in bold_words:
            insert_and_scroll(word, "bold")
        else:
            insert_and_scroll(word)
        if i < len(words) - 1:
            insert_and_scroll(' ')


def start_game(event):
    text_input = input_box.get().upper()
    insert_and_scroll(f"You: {text_input}\n")
    input_box.delete(0, "end")

    while True:
        if text_input == "Y":
            wait()
            insert_and_scroll(Prologue1)
            wait()
            insert_and_scroll(Prologue1_1)
            wait()
            insert_and_scroll(Prologue2)
            wait()
            insert_and_scroll(Prologue3 + "\n", "title")
            wait()
            insert_and_scroll("What is your name, hero?\n\n")
            input_box.bind("<Return>", character_creation)
            break
        elif text_input == "N":
            insert_and_scroll("Have a nice day, then.")
            break
        else:
            insert_and_scroll("Come on, it's not a tough question.\n\n")
            main()
            break

def character_creation(event):
    player_name = input_box.get()
    insert_and_scroll(f"You: {player_name}\n\n")
    input_box.delete(0, "end")
    welcome(player_name)

def welcome(player_name):
    insert_and_scroll(f"Welcome, brave {player_name}.\n\n")
    wait()
    insert_and_scroll("Will you answer the call to adventure? (Y/N):\n\n")
    input_box.unbind("<Return>")
    input_box.bind("<Return>", lambda event, name=player_name: heed_the_call(event, name))

def heed_the_call(event, player_name):
    heed_the_call = input_box.get().upper()
    insert_and_scroll(f"You: {heed_the_call}\n\n")
    input_box.delete(0, "end")

    if heed_the_call == "Y":
        insert_and_scroll(f"May the sun ever light your path, {player_name}.\n\n\n")
        wait()
        intro_opening(event, player_name)

    elif heed_the_call == "N":
        insert_and_scroll("And behold: the land fell into the abyss.\n\n")
        wait()
        insert_and_scroll("The End.")
    else:
        insert_and_scroll("Come on, it's not a tough question.\n\n")
        welcome(player_name)

def intro_opening(event, player_name):
    insert_and_scroll("Prologue: The Hero’s Dream\n\n", "title")
    mixer.init()
    mixer.music.load("/Users/timburns/Music/Logic/Berklee/Before The Flood OST/Leviathan Showdown Loop.mp3")
    mixer.music.play(-1)
    wait()
    insert_and_scroll("Salt water forces its way through your pursed lips. You can’t tell if it’s sweat or sea mist.\nYour senses are bombarded by lightning flashes and the deep drums of thunder.\nWaves crash against the cliff edge, one after the next, each stealing more of the land from underneath you.\n\n")
    wait()
    bold_text("*TUTORIAL* You will encounter decisions on your path, with weighty consequences. Your options will be written in bold text. Respond with one of those bold options, and witness the outcome of your decision.\n\n", ["TUTORIAL", "bold"])
    wait()
    bold_text("Do you understand?\n\n", ["understand?\n\n"])
    input_box.bind("<Return>", lambda event: handle_response(intro_tutorial, event, player_name))

def intro_tutorial(response, player_name):
    if response == "understand":
            insert_and_scroll(f"You catch on quick, {player_name}.\n\n") 
            wait()
            bold_text("You feel the cliff shaking underneath your feet. Do you step back or stand your ground?\n\n", ["step", "stand"])
            input_box.bind("<Return>", lambda event: handle_response(intro_shaking_ground, event, player_name))
    else:
            bold_text("Let's try that again. Do you understand?\n\n", ["understand?\n\n"])
            input_box.bind("<Return>", lambda event: handle_response(intro_tutorial, event, player_name))
            
def intro_shaking_ground(response, player_name):
    if response == "step":
        insert_and_scroll("You step back just in time to see a huge chunk of earth dislodge from the cliff and tumble into the waves below.\n\n")
        wait()
        insert_and_scroll("Then you see it. The shape, writhing through the jagged waves, breaking the surface with an ear-splitting howl, turning its countless heads, eyes, tentacles and teeth... on you.\n\n")
        wait()
        bold_text(f"This is the moment of truth, {player_name}. Do you fight or run away?\n\n", ["fight", "run"])
        input_box.bind("<Return>", lambda event: handle_response(intro_leviathan_battle, event, player_name))
    elif response == "stand":
        insert_and_scroll("You plant your feet, grit your teeth, and find yourself, along with the land you were standing on, plummeting into the ocean.\n\n")
        wait()
        insert_and_scroll("The End.\n\n", "bold")
        wait()
        bold_text("Let's try that again. Do you step back or stand your ground?\n\n", ["step", "stand"])
        input_box.bind("<Return>", lambda event: handle_response(intro_shaking_ground, event, player_name))
    else:
        bold_text("You must decide. Do you step back or stand your ground?\n\n", ["step", "stand"])
        input_box.bind("<Return>", lambda event: handle_response(intro_shaking_ground, event, player_name))

def intro_leviathan_battle(response, player_name):
    if response == "fight":
        insert_and_scroll("And so it begins. You draw your sword and charge the beast.\n\n")
        wait()
        hero = Hero(player_name, 100, 0.2, Weapon("Blade of the Chosen", "Sword", 20, 3000), gui_output=output_box)
        enemy = Leviathan("Leviathan", 999, 0.4, Weapon("Tentacles", "Body", 30, 2000), gui_output=output_box)
        game = Game(hero, enemy, gui_output=output_box)
        while True:

            game.battle()
            wait()
            if game.hero.health <= 0 or game.enemy.health <= 0:
                if game.hero.health <= 0:
                    hero_defeat_text = '''
With every whip of the monster's tentacles, your body grows weaker. You fall to your knees, your sword slipping from your grasp. The beast looms over you, its jaws open wide, ready to swallow you whole. Its breath reeks of stale coffee and last night's wine. Its slimy tentacles grasp your shoulders and start shaking you, while from deep in its cavernous throat, you hear it call your name...\n\n
'''
                    insert_and_scroll(hero_defeat_text)
                    wait()
                    insert_and_scroll(f'"{player_name}... "\n\n')
                    wait()
                    insert_and_scroll(f'"{player_name}... "\n\n')
                    capitalised_player_name = player_name.upper()
                    insert_and_scroll(f'"{capitalised_player_name}!!"\n\n', "bold")
                    wait()
                    mixer.music.load("/Users/timburns/Music/Logic/Berklee/Before The Flood OST/Siempre Tranquillo Loop.mp3")
                    mixer.music.play(-1)
                    insert_and_scroll("You open your eyes to see the looming shape of your mother, shaking you awake.\n\n")
                    wait()
                    insert_and_scroll(f'Mother: "{player_name}! Wake up! The basement... it\'s... they\'re everywhere!"\n\n')
                    wait()
                    bold_text("Do you want to find out what's happening or keep dreaming?\n\n", ["happening", "dreaming?\n\n"])
                    input_box.bind("<Return>", lambda event: handle_response(chapter_one_wake_up, event, player_name))
                if game.enemy.health <= 0:
                    insert_and_scroll("The beast lets out a final, deafening roar, then collapses into the sea, its tentacles thrashing in the water.\n\n")
                    wait()
                    insert_and_scroll("Congratulations, you have beaten the monster and broken the game. Are you happy?\n\n")

                break
                    
    elif response == "run":
        insert_and_scroll("You turn and run, but the beast is faster. It catches you in its jaws and swallows you whole.\n\n")
        wait()
        insert_and_scroll("The End.\n\n", "bold")
        wait()
        bold_text("Let's try that again. Do you fight or run away?\n\n", ["fight", "run"])
        input_box.bind("<Return>", lambda event: handle_response(intro_leviathan_battle, event, player_name))
    else:
        bold_text("You must decide. Do you fight or run away?\n\n", ["fight", "run"])
        input_box.bind("<Return>", lambda event: handle_response(intro_leviathan_battle, event, player_name))

def chapter_one_wake_up(response, player_name):
    if response == "happening":
        insert_and_scroll('You: "What\'s going on? Who are everywhere?"\n\n')
        wait()
        insert_and_scroll(f'Mother: "RATS!"\n\n')
        wait()
        insert_and_scroll('Chapter One: A Midsummer Nightmare\n\n', "title")  
        wait()
        insert_and_scroll('You hurry downstairs after your mother, who waits for you at the basement door, a rolling pin in one hand and a dirty apron in the other.\n\n')
        wait()
        insert_and_scroll(f'Mother: "Take these, {player_name}, and squash those revolting creatures before they nibble the house to pieces!"\n\n')
        bold_text("Are you feeling brave? Do you take the gear, try to persuade your mother to do it herself, or flee back to bed?\n\n", ["take", "persuade", "flee"])
        input_box.bind("<Return>", lambda event: handle_response(chapter_one_rats, player_name))
    elif response == "dreaming":
        insert_and_scroll('You: "Begone, foul beast! My name is not yours to be uttered!"\n\nYou push your mother\'s arms away and roll over.\n\n')
        wait()
        insert_and_scroll(f'Mother: "...? The only foul beasts here are the ones downstairs, and once you\'ve dealt with them we can discuss treating your mother with some respect! Now get UP!"\n\n')
        wait()
        insert_and_scroll('And with that, you find yourself suddenly on the floor, blanket ripped away from you. You thank the skies for your nightclothes.\n\n')
        wait()
        bold_text("One day, you'll find out what happens next. But this is not that day, so let's try again. Do you want to find out what's happening or keep dreaming?\n\n", ["happening", "dreaming?\n\n"])
        input_box.bind("<Return>", lambda event: handle_response(chapter_one_wake_up, player_name))

def chapter_one_rats(response, player_name):
    if response == "take":
        wait()
        insert_and_scroll('You shiver a little - *rats* - and grab the rolling pin and apron, then descend down the dark basement stairs.\nThe squeaking grows louder with every step. Your foot lands on something that squishes under your weight.\n\n')
        wait()
        insert_and_scroll('Its friends don\'t seem pleased with you.\n\n')
        hero = Hero(player_name, 20, 0.05, Weapon("Rolling Pin", "Tool", 2, 1), gui_output=output_box)
        enemy = Rat("Rat Swarm", 15, 0.1, Weapon("Teeth", "Body", 1, 1), gui_output=output_box)
        game = Game(hero, enemy, gui_output=output_box)
        while True:

            game.battle()
            wait()
            if game.hero.health <= 0 or game.enemy.health <= 0:
                if game.hero.health <= 0:
                    hero_defeat_text = '''
You can't seem to find your groove with this rolling pin. It seems you didn't inherit the dream-you's skills. You head gets faint from blood loss, and you slump to the ground, barely conscious of the swarm of rodents preparing for an easy meal.\n\n
'''
                    insert_and_scroll(hero_defeat_text)
                    wait()
                    insert_and_scroll("The End.\n\n", "bold")
                
                if game.enemy.health <= 0:
                    insert_and_scroll("\nYou've spent many hours honing your skills at the town fayre, and it shows. The rats are no match for your rolling pin.\n\n")
                break
    elif response == "persuade":
        wait()
        bold_text('How will you convince her? Do you appeal to her maternal instincts, call her a coward or attempt a bribe?\n\n', ["instincts", "coward", "bribe?\n\n"])
    elif response == "flee":
        wait()
        insert_and_scroll('You: "Nope!"\n\nYou turn and sprint back to your room, slamming the door behind you.\n\n')



main()

window.mainloop()