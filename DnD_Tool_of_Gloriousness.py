#!/usr/bin/python3
import os
import DnD
import json
import random






def character_menu_selection(menu_entry):
    # if entry <= 4 instantiate Characters() and prompt for a character name to modify
    if menu_entry <= 5 and menu_entry != 2:
        characters = DnD.Characters()
        character_name = input('Enter character name: \n').lower()

        if menu_entry == 4:
            while True:
                try:
                    print(characters.list_character_stats(character_name))
                    character_stat = input('Enter stat name: \n')
                    new_stat = int(input('Enter new stat value: \n'))

                except ValueError:
                    print('Enter a number, not a string.')

                break

        menu_options = {1: characters.create_character(character_name), 2: characters.list_characters(),
                        3: characters.list_character_stats(character_name),
                        4: characters.change_stat(character_name, character_stat, new_stat),
                        5: characters.remove_character(character_name)}


def moonser_menu_selection(menu_entry):
    # if entry >= 6 instantiate monsters() and prompt for a monster name to modify
    elif menu_entry >= 6 and menu_entry <= 10:
        monsters = DnD.Monsters()
        monster_name = input('Enter monster name: \n').lower())

    # add monster
    if menu_entry == 7:
       monsters = DnD.Monsters()
       monster_name = input('Enter monster name: \n')

    # get a stat or update one
    elif menu_entry == 7 or menu_entry == 7:
        monster_name = input('Enter monster name: \n').lower())

        if menu_entry == 7:
            print(get_monster_stat(monster_name, monster_stat))

        elif menu_entry == 7:
            try:
                mons_new_stat = int(input('Enter new stat value: \n'))
            except ValueError:
                print('Enter a number, not a string.')
                main()
            # attempt to add the stat
            change_monster_stat(monster_name, monster_stat, new_stat)
            print('Done')

    # single die roll
    if menu_entry == 7:
        sides = int(input('Enter amount of sides: \n'))
        print(roll_die(sides))

    # multi-die roll
    if menu_entry == 10:
        total_dice = int(input('Number of dice to throw? \n'))
        sides = int(input('Enter amount of sides: \n'))
        while total_dice > 0:
            print(roll_die(sides))
            total_dice -= 1

    # simulate a battle (still half broken HP updates?)
    if menu_entry == 10:
        character_name = input('Enter character name: \n')
        monster_name = input('Enter monster name: \n')
        battle_simulator(character_name, monster_name)



def main():
    print('\nPress \'q\' to quit or go back.')
    while True:
        print('What would you like to do? \n')

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
        print('12) Roll XdX')
        print('13) Battle simulator')
        print('q) Quit \n')

        menu_entry = input()
        if menu_entry == 'q':
            exit(print('Bye bye!'))

        else:
            menu_entry = int(menu_entry)
            menu_selection(menu_entry)
