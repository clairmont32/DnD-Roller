"""
Given a character and a monster, calculate the attack, damage, and hit rolls for each
then compare the two to determine a winner per each roll until either dies.

Each roll for each actor must be displayed for QA checks and end-user curiosity for stat growth

"""

import json
import random
import monsters



def add_character_stats():
    with open('characters.json', 'r+') as character_file:
        characters = json.load(character_file)

        name = str(input('Enter character name: \n'))
        armorClass = int(input('Enter armor class: \n'))
        initiative = int(input('Enter initiative: \n'))
        hitPoints = int(input('Enter HP: \n'))
        attackHit = int(input('Enter attack hit: \n'))
        damageDice = int(input('Enter damage dice number: \n'))
        damageBonus = int(input('Enter damage bonus: \n'))
        cure = int(input('Enter cure: \n'))
        numAttacks = int(input('Enter number of attacks: \n'))

        characters = {'armorClass': armorClass, 'initiative': initiative, 'hitPoints': hitPoints,
                            'attackHit': attackHit, 'damageDice': damageDice, 'damageBonus': damageBonus,
                            'cure': cure, 'numAttacks': numAttacks}

        character_file.truncate(0)
        character_file.writelines(json.dumps(characters))



# roll a die with a given amount of sides
def roll_die(sides):
    result = random.randint(1, sides)
    return result

# calculate attack roll for player
#def attack_roll(player):
 #   return player[attackHit]


add_character_stats()