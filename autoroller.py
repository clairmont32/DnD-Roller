"""
Given a character and a monster, calculate the attack, damage, and hit rolls for each
then compare the two to determine a winner per each roll until either dies.

Each roll for each actor must be displayed for QA checks and end-user curiosity for stat growth

"""

import json
import random
import monsters


# prompt for and add character stats to json file
def add_character_stats():
    # read current character stats in json dictionary for
    with open('characters.json', 'r') as file:
        characters = json.load(file)

    # prompt for character stats
    name = str(input('Enter character name: \n'))
    armor_class = input('Enter armor class: \n')
    initiative = input('Enter initiative: \n')
    hit_points = input('Enter HP: \n')
    attack_hit = input('Enter attack hit: \n')
    damage_dice = input('Enter damage dice number: \n')
    damage_bonus = input('Enter damage bonus: \n')
    cure = input('Enter cure: \n')
    num_attacks = input('Enter number of attacks: \n')

    # add to json
    characters[name] = {
        "armor_class": armor_class,
        "initiative": initiative,
        "hit_points": hit_points,
        "attack_hit": attack_hit,
        "damage_dice": damage_dice,
        "damage_bonus": damage_bonus,
        "cure": cure,
        "num_attacks": num_attacks
    }

    # delete the old data and write the new
    with open('characters.json', 'r+') as file:
        file.truncate(0)
        file.write(json.dumps(characters))

    return


# roll a die with a given amount of sides
def roll_die(sides):
    result = random.randint(1, sides)
    return result

# calculate attack roll for player
#def attack_roll(player):
 #   return player[attackHit]


add_character_stats()