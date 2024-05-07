# Final Project (Text Adventure Game)

## What Is It?

'Before The Flood' is a text adventure game loosely based on elements of Hebrew/Christian mythology and cosmology. It's written in Python and made using a built-in Python GUI called Tkinter. I tried multiple other GUI options (including RenPy and Pygame) but settled on Tkinter firstly because it's so "basic" in the language - it's native to Python - and secondly for its adaptability. As I continue to develop this game, I may decide to move to a different GUI, but for now I'm appreciating how versatile the Tkinter module is.

## What Inspired Me?

This project was inspired by a conversation I had with my wife, in which she reminisced about Choose Your Own Adventure books from childhood. It was also inspired by a desire to explore and further contemplate some theology and philosophy - as all good video games should seek to do, of course. I set out to design a game with an interesting story, philosophical depth, engaging mechanics and constant surprises. I'm not sure I've succeeded at any of the above so far, but I'm on my way.

## System Flow

### Basics

The Tkinter interface is made up of two primary widgets: an "input box" (or Text Entry) for player input, and on "output box" to display the game's content (the latter serving in place of a terminal console). The majority of the game is made up of functions which each follow one particular player decision. Players will be given options, and they type a keyword linked to the option they choose to progress the story in the direction of their choosing. For example, at one point the player has to make this choice:

"You feel the cliff shaking underneath your feet. Do you **step** back or **stand** your ground?""

If the player types "step" and hits return, this text will be displayed:

```"You step back just in time to see a huge chunk of earth dislodge from the cliff and tumble into the waves below."```

And, unfortunately, if they choose "stand":

```"You plant your feet, grit your teeth, and find yourself, along with the land you were standing on, plummeting into the ocean."```

### Battles

Also present at points in the game are battles. Here, I've learnt how to use classes to create a blueprint for the hero and their opponents, and then to implement those blueprints into any instance of battle. The current battle itself plays out automatically, but using some moderately detailed mathematics to add complexity to the results. I've created classes for Character (and the subclass of each individual character), Weapon and HealthBar, as well as a class of Game (which should be renamed battle) to set-up each instance of battle.

### Music

The game uses the mixer in Pygame to play audio, which triggers at different points in the game. So far there are two cues in the game based around the same motif, with more to come as the game develops.

## What Works?

Well, most of the game as it stands right now. There are incomplete story branches yet to be filled out, but they will come as I write & code in more of the plot. I'm very happy with the flow of the story and how each event triggers.

### Classes

I'm particularly proud of the Character class and its complexity. Each character thus far has a name, a personalised health bar, a weapon attribute and a critical hit probability. Their damage-per-round is equal to a random integer in the range of

```(weapon_damage - int(0.25*weapon_damage)), (weapon_damage + int(0.25*weapon_damage))```

and they score a critical hit in a round when a random integer is created which is less than or equal to their crit chance.

### Format

I'm also proud of the functionality of the format. The timing of each new line, the fact that the most crucial text for the current moment is always easy to be read, and particularly the "bold_word" function, in which the program searches through a string to find the mentioned words and assign them as bold, are all things I'm happy with.

## What's Not So Hot?

The audio doesn't loop seamlessly, there are no visuals, and the game uses far too much CPU.

## What Comes Next?

### Visuals

As mentioned above, I want to incorporate visuals in the game, specifically scene backgrounds. I'd like to have a translucent image underneath every major event to add story immersion, and Tkinter isn't set up for that. I'll either need to migrate to another GUI, or do some heavy hotwiring of Tkinter to make it work.

### Battle Mechanics

I want to make the battles more interactive. Like any good RPG in the D&D/Final Fantasy tradition, I want to give players a list of options to choose from when engaging in battle, and in order to do that I need to build up the character mechanics even more, so armour, weapons, spells etc can be collected and utilised in battle.

### Character Traits

I'd also like to develop the personality of the hero character, allowing them to play to their strengths in each interaction. One player may use their Charisma stat to win over a guard, but another would use Subtlety to sneak their way around him instead. This will again require adding complexity to the Character class.

### Story

I just want to finish the story! There's a long way to go yet.
