## DnD DM Tool ##

A text-based character stat manager and battle simulator that is being developed for a friend's discord D&D game. Character stat management is done via json files (characters.json/monsters.json). Direct manipulation of these files is *NOT* advised and is easily done through the script.

#### Battle ####
Battle is done in a modular form by doing each action of the battle as a separate method or function. Initiative checks are performed at the start of battle, with damage bonuses and a lost health limitor as additional options. Health points are automatically deducted upon calculation to ensure that monsters, players, or NPCs can be killed mid-battle. 

The battle simulator does not continually calculate attacks and apply damage. To ensure DMs can adjust the rolls in a fluid fashion attacks take place and are paused until the DM hits 'Enter' to ensure he/she is aware of what took place and can quit before any damage is applied. This allows the DM to stop/pause battle, update any stats to either party, then continue battle.

##### SPELLS ARE NOT IMPLEMENTED CURRENTLY DUE TO THE EXTENSIVE AMOUNT OF DATA AND VARYING SITUATIONS THEY MAY CALL FOR #####

Single attacks will be added shortly to account for various roleplaying circumstances (ambushes, stealth kills, punches, etc).

#### Feature List ####
 - Add a new character
 - List all characters
 - List a character's stats
 - Update a character's stats
 - Remove a character
 - Add a new monster
 - List all monsters
 - List a monster's stats
 - Update a monster's stats
 - Remove a monster
 - Roll a single dX
 - Roll a XdX
 - Battle simulator

##### Feature Requests #####
If there is a feature you'd like to see added, please submit an issue. If you've already developed a feature or fixed a bug, please submit a pull request.
