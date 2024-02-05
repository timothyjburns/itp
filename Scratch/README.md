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

-
