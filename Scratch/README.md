# Scratch Project Documentation

## What I Did

- Chose the "Shark 2" sprite & "Underwater 1" background

- Named the project "Shark Attack"

- Added the "Fish" sprite

- Created scripts for movement 10 places up, down, left and right when the respective key is pressed

*PROBLEM* The fish will only move in one direction at a time; if two keys are pressed, only the latter of the two registers.

*SOLUTION* Reframed the scripts as "When flag is pressed, if" scripts with a second tier for the second direction.

*PROBLEM* Nothing happens when the green flag is pressed.

*SOLUTION* Found at https://scratch.mit.edu/help/studio/tips/howto/hide5/#:~:text=Click%20the%20Events%20category.,you%20want%20it%20to%20stop. Added a "forever" element to the scripts.

*PROBLEM* "up" and "down" directions only function when an x-axis key is pressed simultaneously.

*SOLUTION* Added an "if not right & left pressed then move y-axis" script for both "up" and "down" keys.

- Added a "when flag is pressed" script for the shark, with a "go to Fish" command

*PROBLEM* It jumped straight to the fish rather than moving slowly as I desired.

*SOLUTION* Changed command to "glide 1 second to Fish"

- Added an increasing threat: "repeat x times" script for "glide y", where y halves whenever x doubles.

- Added "if distance to Fish < 40 then change to costume B" for Shark

*PROBLEM* Shark is now stuck in costume B

*SOLUTION* Changed the script to be within a separate "When green flag clicked" script.

- Added "if distance to Fish < 20 broadcast message1", then added two "when I receive message 1" scripts for the Fish that cause it to trigger a scream, rotate, and move into the top right corner

*PROBLEM* I want this to "end" the game but it doesn't.

*SOLUTION* I added a "stop all" script for after 40 repeats of the rotate & move script

- Added an 8-bit Jaws theme that starts when the flag is clicked and ends when message1 is broadcasted

*PROBLEM* The game is too easy - I can escape the shark easily

*SOLUTION* Added more glide commands with smaller timeframes to increase shark speed.

*PROBLEM* The shark now can follow the fish when message1 is broadcasted so the game doesn't end.

*SOLUTION* Added "when I receive message1 stop other scripts in sprite" script.
