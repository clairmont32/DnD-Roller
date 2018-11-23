#!/usr/bin/python3
import os
import DnD
import json
import random


def character_menu_selection(menu_entry):
    characters = DnD.Characters()

    if menu_entry == 1 or menu_entry >= 3:
        character_name = input('Enter character name: \n').lower()

        if menu_entry == 1:
            characters.create_character(character_name)

        elif menu_entry == 3:
            characters.list_character_stats(character_name)

        elif menu_entry == 4:
            while True:
                try:
                    characters.list_character_stats(character_name)
                    character_stat = input('Enter stat name: \n')
                    new_stat = int(input('Enter new stat value: \n'))
                    characters.change_stat(character_name, character_stat, new_stat)

                except ValueError:
                    print('Enter a number, not a string.')

                break

        elif menu_entry == 5:
            characters.remove_character(character_name)

    elif menu_entry == 2:
        characters.list_characters()


def monster_menu_selection(menu_entry):
    monsters = DnD.Monsters()

    if menu_entry in range(6, 11) and menu_entry != 7:
        monster_name = input('Enter monster name: \n').lower()

        if menu_entry == 6:
            monsters.create_monster(monster_name)

        if menu_entry == 8:
            monsters.list_monster_stats(monster_name)

        if menu_entry == 9:
            while True:
                try:
                    print(monsters.list_monster_stats(monster_name))
                    monster_stat = input('Enter stat name: \n')
                    new_stat = int(input('Enter new stat value: \n'))
                    monsters.change_stat(monster_name, monster_stat, new_stat)

                except ValueError:
                    print('Enter a number, not a string.')

                break

        if menu_entry == 10:
            monsters.remove_monster(monster_name)
        
    elif menu_entry == 7:
        monsters.list_monsters()


def roll_die(sides):
    if sides > 0:
        print(random.randint(1, sides))

    else:
        print('Enter an integer greater than 0!')


def conduct_combat():
    # simulate a battle (still half broken HP updates?
    character_name = input('Enter character name: \n')
    monster_name = input('Enter monster name: \n')
    battle = DnD.Battle(character_name, monster_name)
    aggro_level = battle.attack_aggressiveness()

    while True:
        battle.commence_attack(aggro_level)
        quit_continue_battle = input('Press enter to continue or \'q\' to quit to menu. \n')
        if quit_continue_battle == 'q':
            return


def main():

    # print main menu
    while True:
        print('What would you like to do?')

        print('1) Add a new character')
        print('2) List all characters')
        print('3) List a character\'s stats')
        print('4) Update a character\'s stats')
        print('5) Remove a character')
        print('6) Add a new monster')
        print('7) List all monsters')
        print('8) List a monster\'s stats')
        print('9) Update a monster\'s stats')
        print('10) Remove a monster')
        print('11) Roll a single dX')
        print('12) Roll a XdX')
        print('13) Battle simulator')
        print('q) Quit \n')

        menu_entry = input()

        # if 'q' or a number is entered quit. If not, re-prompt.
        if menu_entry == 'q':
            exit(print('Bye bye!'))

        elif menu_entry.isalpha():
            print('\nPlease enter \'q\' or a number \n\n')

        # do a sanity check on the entry for numbers
        elif menu_entry.isnumeric():
            menu_entry = int(menu_entry)

            if menu_entry in range(1, 6):
                character_menu_selection(menu_entry)

            elif menu_entry in range(6, 11):
                monster_menu_selection(menu_entry)

            # single-die roll
            elif menu_entry == 11:
                while True:
                    try:
                        sides = int(input('Enter amount of sides: \n'))
                    except ValueError:
                        print('Enter an integer')

                    break

                roll_die(sides)
                input('Press enter to return to the menu. \n\n')

            # multi-die roll
            elif menu_entry == 12:
                while True:
                    try:
                        total_dice = int(input('Number of dice to throw? \n'))
                        sides = int(input('Enter amount of sides: \n'))
                    except ValueError:
                        print('Enter an integer')
                    break

                while total_dice > 0:
                    roll_die(sides)
                    total_dice -= 1
                input('Press enter to return to the menu. \n\n')

            elif menu_entry == 13:
                conduct_combat()


if __name__ == '__main__':
    main()
