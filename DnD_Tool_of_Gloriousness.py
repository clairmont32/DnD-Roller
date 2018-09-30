"""
Given a character and a monster, calculate the attack, damage, and hit rolls for each
then compare the two to determine a winner per each roll until either dies.

Each roll for each actor must be displayed for QA checks and end-user curiosity for stat growth

"""
import os
import json
import random


def file_checks():
    cwd = os.getcwd()
    if os.path.exists('characters.json') is False:
        print('Could not find characters.json in '.format(cwd))

    if os.path.exists('monsters.json') is False:
        print('Could not find monsters.json in '.format(cwd))


# prompt for and add character stats to json file
def add_character():
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
    with open('characters.json', 'w') as file:
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


# update character stat due to combat or other influence 
def change_character_stat(name, stat, new_stat):
    with open('characters.json', 'r') as characters_file:
        characters = json.load(characters_file)

    try:
        characters[name].update({stat: new_stat})
    except KeyError as ker:
        print('Could not update {!s}'.format(new_stat))
        print(ker)

    with open('characters.json', 'w') as characters_file:
        characters_file.truncate(0)
        characters_file.write(json.dumps(characters))


# update monster stat due to combat or other influence 
def change_monster_stat(name, stat, new_stat):
    with open('monsters.json', 'r') as monsters_file:
        monsters = json.load(monsters_file)

    try:
        monsters[name].update({stat: new_stat})
    except KeyError as ker:
        print('Could not update {!s}'.format(new_stat))
        print(ker)

    with open('monsters.json', 'w') as monsters_file:
        monsters_file.truncate(0)
        monsters_file.write(json.dumps(monsters))


# prompt for and add monster stats to json file
def add_monster():
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
    with open('monsters.json', 'w') as file:
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


# compare initiative to see who goes first
def battle_simulator(character_name, monster_name):
    char_initiative = get_character_stat(character_name, 'initiative')
    mons_initiative = get_monster_stat(monster_name, 'initiative')

    if mons_initiative > char_initiative:
        do_monster_attack(character_name, monster_name)
        do_character_attack(character_name, monster_name)

    elif mons_initiative < char_initiative:
        do_character_attack(character_name, monster_name)
        do_monster_attack(character_name, monster_name)

    elif mons_initiative == char_initiative:
        do_character_attack(character_name, monster_name)
        do_monster_attack(character_name, monster_name)


# perform single character attack
def do_character_attack(character_name, monster_name):
    with open('monsters.json', 'r') as monsters_file:
        all_mons = json.load(monsters_file)

    with open('characters.json', 'r') as characters_file:
        all_chars = json.load(characters_file)

    # extracting only the profiles we care about
    mons = all_mons[monster_name]
    char = all_chars[character_name]

    # roll d20
    char_attack_roll = roll_die(20)

    if char['hitPoints'] <= 0:
        print('{!s} has been killed!'.format(character_name))
        exit(0)

    # compare if roll stats are greater than character's armor, subtract damage from players health
    # perform health check and display new values
    elif (char_attack_roll + char['attackHit']) > mons['armorClass']:
        print('{!s} hit {!s} for {!s} damage'.format(character_name, monster_name, char['damageDice']))
        new_char_health = mons['hitPoints'] - char['damageDice']
        change_character_stat(character_name, 'hitPoints', new_char_health)
        print('{!s} has {!s} HP left.'.format(monster_name, new_char_health))

    # failed it
    else:
        print('{!s} did not hit above {!s}\'s armor class!'.format(character_name, monster_name))


# perform single monster attack
def do_monster_attack(character_name, monster_name):
    with open('monsters.json', 'r') as monsters_file:
        all_mons = json.load(monsters_file)

    with open('characters.json', 'r') as characters_file:
        all_chars = json.load(characters_file)

    # extracting only the profiles we care about
    mons = all_mons[monster_name]
    char = all_chars[character_name]

    # roll d20
    mons_attack_roll = roll_die(20)

    if mons['hitPoints'] <= 0:
        print('{!s} has been killed!'.format(monster_name))
        exit(0)

    # compare if roll stats are greater than character's armor, subtract damage from players health
    # perform health check and display new values
    elif (mons_attack_roll + mons['attackHit']) > char['armorClass']:
        print('{!s} hit {!s} for {!s} damage'.format(monster_name, character_name, mons['damageDice']))
        new_char_health = char['hitPoints'] - mons['damageDice']
        change_monster_stat(monster_name, 'hitPoints', new_char_health)
        print('{!s} has {!s} HP left.'.format(character_name, new_char_health))

    # failed it
    else:
        print('{!s} did not hit above {!s}\'s armor class!'.format(monster_name, character_name))


# setup and start main menu while loop
def main():
    file_checks()

    print('\nPress \'q\' to quit or go back.')
    while True:
        print('What would you like to do? \n')
        print('1) Add a new character')
        print('2) Get a character\'s specific stat')
        print('3) Update a character\'s stats')
        print('4) Add a new monster')
        print('5) Get a monster\'s specific stat')
        print('6) Update a monster\'s stats')
        print('7) Roll a single dX')
        print('8) Roll XdX')
        print('9) Battle simulator')
        print('q) Quit \n')

        menu_entry = input()
        if menu_entry == 'q':
            exit(print('Bye bye!'))
        else:
            menu_entry = int(menu_entry)

            # add character
            if menu_entry == 1:
                add_character()

            # get a stat or update one
            elif menu_entry == 2 or menu_entry == 3:
                character_name = input('Enter character name: \n')
                character_stat = input('Enter character stat: \n')

                if menu_entry == 2:
                    print(get_character_stat(character_name, character_stat))

                elif menu_entry == 3:
                    new_stat = int(input('Enter new stat value: \n'))
                    print(change_character_stat(character_name, character_stat, new_stat))
                    print('Done')

            # add monster
            if menu_entry == 4:
                add_monster()

            # get a stat or update one
            elif menu_entry == 5 or menu_entry == 6:
                monster_name = input('Enter monster name: \n')
                monster_stat = input('Enter monster stat: \n')

                if menu_entry == 5:
                    print(get_monster_stat(monster_name, monster_stat))

                elif menu_entry == 6:
                    new_stat = int(input('Enter new stat value: \n'))
                    change_monster_stat(monster_name, monster_stat, new_stat)
                    print('Done')

            # single die roll
            if menu_entry == 7:
                sides = int(input('Enter amount of sides: \n'))
                print(roll_die(sides))

            # multi-die roll
            if menu_entry == 8:
                total_dice = int(input('Number of dice to throw? \n'))
                sides = int(input('Enter amount of sides: \n'))
                while total_dice > 0:
                    print(roll_die(sides))
                    total_dice -= 1

            # simulate a battle (still half broken HP updates?)
            if menu_entry == 9:
                character_name = input('Enter character name: \n')
                monster_name = input('Enter monster name: \n')
                battle_simulator(character_name, monster_name)


main()
