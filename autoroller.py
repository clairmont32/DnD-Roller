"""
Given a character and a monster, calculate the attack, damage, and hit rolls for each
then compare the two to determine a winner per each roll until either dies.

Each roll for each actor must be displayed for QA checks and end-user curiosity for stat growth

"""
import os
import json
import random
import monsters


def __init__():
    cwd = os.getcwd()
    if os.path.exists('characters.json') is False:
        print('Could not find characters.json in '.format(cwd))

    if os.path.exists('monsters.json') is False:
        print('Could not find monsters.json in '.format(cwd))


# prompt for and add character stats to json file
def add_change_character():
    # read current character stats in json dictionary for
    with open('characters.json', 'r') as file:
        characters = json.load(file)

    # prompt for character stats
    name = str(input('Enter character name: \n'))
    armor_class = int(input('Enter armor class: \n'))
    initiative = int(input('Enter initiative: \n'))
    hit_points = int(input('Enter HP: \n'))
    attack_hit = int(input('Enter attack hit: \n'))
    damage_dice = int(input('Enter damage dice number: \n'))
    damage_bonus = int(input('Enter damage bonus: \n'))
    cure = int(input('Enter cure: \n'))
    num_attacks = int(input('Enter number of attacks: \n'))

    # add to json
    characters[name] = {
        "armorClass": armor_class,
        "initiative": initiative,
        "hitPoints": hit_points,
        "attackHit": attack_hit,
        "damageDice": damage_dice,
        "damageBonus": damage_bonus,
        "cure": cure,
        "numAttacks": num_attacks
    }

    # delete the old data and write the new
    with open('characters.json', 'r+') as file:
        file.truncate(0)
        file.write(json.dumps(characters))

    return


# return single stat from a character
def get_character_stat(name, stat):
    with open('characters.json', 'r') as characters_file:
        characters = json.load(characters_file)

    try:
        character_stats = characters[name]
    except KeyError:
        print('{!s} does not have a character profile saved!'.format(name))

    try:
        requested_stat = character_stats[stat]
        return requested_stat

    except KeyError:
        print('{!s} does not have {!s}'.format(name, stat))


# prompt for and add monster stats to json file
def add_change_monster():
    # read current monster stats in json dictionary for
    with open('monsters.json', 'r') as file:
        monsters = json.load(file)

    # prompt for monster stats
    name = str(input('Enter monster name: \n'))
    armor_class = int(input('Enter armor class: \n'))
    initiative = int(input('Enter initiative: \n'))
    hit_points = int(input('Enter HP: \n'))
    attack_hit = int(input('Enter attack hit: \n'))
    damage_dice = int(input('Enter damage dice number: \n'))
    damage_bonus = int(input('Enter damage bonus: \n'))
    num_attacks = int(input('Enter number of attacks: \n'))

    # add to json
    monsters[name] = {
        "armorClass": armor_class,
        "initiative": initiative,
        "hitPoints": hit_points,
        "attackHit": attack_hit,
        "damageDice": damage_dice,
        "damageBonus": damage_bonus,
        "numAttacks": num_attacks
    }

    # delete the old data and write the new
    with open('monsters.json', 'r+') as file:
        file.truncate(0)
        file.write(json.dumps(monsters))

    return


# return single stat from a monster
def get_monster_stat(name, stat):
    with open('monsters.json', 'r') as monsters_file:
        monsters = json.load(monsters_file)

    try:
        monster_stats = monsters[name]
    except KeyError:
        print('{!s} does not have a monster profile saved!'.format(name))

    try:
        requested_stat = monster_stats[stat]
        return requested_stat
    
    except KeyError:
        print('{!s} does not have {!s}'.format(name, stat))


# roll a die with a given amount of sides
def roll_die(sides):
    result = random.randint(1, sides)
    return result


def do_character_attack(character_name, monster_name):
    char_hit_points = get_character_stat(character_name, 'hitPoints')
    char_damage_bonus = get_character_stat(character_name, 'damageBonus')
    char_attack_hit = get_character_stat(character_name, 'attackHit')
    char_damage_dice = get_character_stat(character_name, 'damageDice')

    monster_damage_bonus = get_monster_stat(monster_name, 'damageBonus')
    monster_hit_points = get_monster_stat(monster_name, 'hitPoints')
    monster_armor_class = get_monster_stat(monster_name, 'armorClass')

    char_attack_roll = roll_die(20)
    if (char_attack_roll + char_attack_hit) > monster_armor_class:
        print('Hit for {!s} damage'.format(char_damage_dice))
        monster_hit_points -= char_damage_dice
        print('{!s} has {!s} HP left.'.format(monster_name, monster_hit_points))
        if monster_hit_points <= 0:
            print('{!s} has been killed!'.format(monster_name))
            print('{!s} has {!s} health left.'.format(character_name, char_hit_points))
            return

    else:
        print('{!s} did not hit above {!s}\'s armor class!'.format(character_name, monster_name))


do_character_attack('jon', 'vampireSpawn')

