#!/usr/bin/python3
import os
import json
import random
from DnD_Tool_of_Gloriousness import main as main_menu


# means of interacting with characters in characters.json
class Characters:
    def __init__(self):
        cwd = os.getcwd()
        if os.path.exists('characters.json') is False:
            exit(print('Could not find characters.json in {!s}'.format(cwd)))

        with open('characters.json', 'r') as characters_file:
            self.characters = json.load(characters_file)

    # creates an empty character in characters.json
    def create_character(self, character_name):
        self.characters[character_name] = {}

        with open('characters.json', 'w') as characters_file:
            characters_file.truncate(0)
            characters_file.write(json.dumps(self.characters))
        Characters.add_stats(self, character_name)

    # removes a character from characters.json
    def remove_character(self, character_name):
        try:
            del self.characters[character_name]
            with open('characters.json', 'w') as characters_file:
                characters_file.truncate(0)
                characters_file.write(json.dumps(self.characters))

            print('Removed {!s} from characters list'.format(character_name))

        except KeyError:
            print('{!s} does not have a character profile saved!'.format(character_name))

        input('Press enter to continue.\n')

    # lists current character names
    def list_characters(self):
        [print(name) for name in self.characters.keys()]
        input('\n Press Enter to continue. \n')

    # prompt for character stats
    def add_stats(self, character_name):
        print('Enter numeric values for the below stats- ')
        while True:
            try:
                armor_class = int(input('Enter armor class: \n'))
                initiative = int(input('Enter initiative: \n'))
                hit_points = int(input('Enter HP: \n'))
                attack_hit = int(input('Enter attack hit: \n'))
                damage_dice = int(input('Damage die roll (1dX): \n'))
                str_modifier = int(input('Enter strength modifier: \n'))
                dex_modifier = int(input('Enter dexterity modifier: \n'))
                cure = int(input('Enter cure: \n'))
                num_attacks = int(input('Enter number of attacks: \n'))
                proficiency = int(input('Enter proficiency bonus: \n'))
                break
            except ValueError:
                print('You didn\'t enter a number!')

        # add to json
        self.characters[character_name] = {"armorClass": armor_class, "initiative": initiative, "hitPoints": hit_points,
                                           "attackHit": attack_hit, "damageDice": damage_dice,
                                           "strModifier": str_modifier, "dexModifier": dex_modifier, "cure": cure,
                                           "numAttacks": num_attacks, "proficiency": proficiency}

        with open('characters.json', 'w') as characters_file:
            characters_file.truncate(0)
            characters_file.write(json.dumps(self.characters))

        print('Stats added. \n')
        input('Press enter to continue \n')

    # lists stats for a given character
    def list_character_stats(self, character_name):
        try:
            for stat, value in self.characters[character_name].items():
                print(stat + ':', value)
            print('\n')

        except KeyError:
            print('{!s} does not have a character profile saved!'.format(character_name))
            input('Press enter to continue...\n')
            main_menu()

        input('Press enter to continue. \n')

    # updates a current stat
    def change_stat(self, character_name, stat, new_stat):
        try:
            self.characters[character_name].update({stat: new_stat})
        except KeyError as ker:
            print('Could not update {!s}'.format(new_stat))
            print(ker)
            main_menu()

        with open('characters.json', 'w') as characters_file:
            characters_file.truncate(0)
            characters_file.write(json.dumps(self.characters))

        print('{!s} {!s} updated to {!s}.'.format(character_name, stat, new_stat))

        input('Press enter to continue. \n')


# means of interacting with monsters in monsters.json
class Monsters:
    def __init__(self):
        cwd = os.getcwd()

        if os.path.exists('monsters.json') is False:
            exit(print('Could not find monsters.json in '.format(cwd)))

        with open('monsters.json', 'r') as monsters_file:
            self.monsters = json.load(monsters_file)

    # creates an empty monster in monsters.json
    def create_monster(self, monster_name):
        self.monsters[monster_name] = {}

        with open('monsters.json', 'w') as monsters_file:
            monsters_file.truncate(0)
            monsters_file.write(json.dumps(self.monsters))
        self.add_stats(monster_name)

    # removes a monster from monsters.json
    def remove_monster(self, monster_name):
        try:
            del self.monsters[monster_name]
            with open('monsters.json', 'w') as monsters_file:
                monsters_file.truncate(0)
                monsters_file.write(json.dumps(self.monsters))

            print('Removed {!s} from characters list'.format(monster_name))

        except KeyError:
            print('{!s} does not have a monster profile saved!'.format(monster_name))

        input('Press enter to continue... \n')

    # lists current monster names
    def list_monsters(self):
        [print(name) for name in self.monsters.keys()]
        input('Press enter to continue... \n')

    # prompt for monster stats
    def add_stats(self, monster_name):
        print('Enter numeric values for the below stats- ')
        while True:
            try:
                armor_class = int(input('Enter armor class: \n'))
                initiative = int(input('Enter initiative: \n'))
                hit_points = int(input('Enter HP: \n'))
                attack_hit = int(input('Enter attack hit: \n'))
                damage_dice = int(input('Damage die roll (1dX): \n'))
                num_attacks = int(input('Enter number of attacks: \n'))
                default_hp = int(input('Enter default HP'))
                break

            except ValueError:
                print('You didn\'t enter a number!')

        # add to json
        self.monsters[monster_name] = {"armorClass": armor_class, "initiative": initiative, "hitPoints": hit_points,
                                       "attackHit": attack_hit, "damageDice": damage_dice, "numAttacks": num_attacks,
                                       "defaultHP": default_hp}

        with open('monsters.json', 'w') as monsters_file:
            monsters_file.truncate(0)
            monsters_file.write(json.dumps(self.monsters))

        print('\n')
        print('Stats added!')
        input('Press enter to continue... \n')

    # lists stats for a given monster
    def list_monster_stats(self, monster_name):
        try:
            for stat, value in self.monsters[monster_name].items():
                print(stat + ':', value)

        except KeyError:
            print('{!s} does not have a monster profile saved!'.format(monster_name))

        input('Press enter to continue... \n')

    # updates a current stat for a named monster
    def change_stat(self, monster_name, stat, new_stat):
        try:
            self.monsters[monster_name].update({stat: new_stat})

        except KeyError as ker:
            print('Could not update {!s}'.format(new_stat))
            print(ker)

        with open('monsters.json', 'w') as monsters_file:
            monsters_file.truncate(0)
            monsters_file.write(json.dumps(self.monsters))

        print('{!s} {!s} updated to {!s}.'.format(monster_name, stat, new_stat))
        input('Press enter to continue... \n')


class Battle(object):
    def __init__(self, character_name, monster_name, advantage):
        super(Characters)
        super(Monsters)
        self.character_name = character_name
        self.monster_name = monster_name

        try:
            with open('characters.json', 'r') as characters_file:
                characters = json.load(characters_file)
                self.char = characters[character_name]
                self.char_init = int(self.char['initiative'])

                # do a quick health check to ensure it's actually alive
                if self.char['hitPoints'] <= 0:
                    print('{!s} has been killed! \n'.format(self.character_name))
                    input('Press enter to continue... \n')
                    main_menu()

        except KeyError:
            print('{!s} does not exist. Please ensure the spelling/capitalization is '
                  'correct or reference the character list'.format(character_name))
            main_menu()

        try:
            with open('monsters.json', 'r') as monsters_file:
                monsters = json.load(monsters_file)
                self.mons = monsters[monster_name]
                self.mons_init = int(self.mons['initiative'])

                # do a quick health check to ensure it's actually alive
                if self.mons['hitPoints'] <= 0:
                    print('{!s} has been killed! \n'.format(self.monster_name))
                    self.reset_monster_health()
                    main_menu()

                    # force reload of __init__ because of an odd condition
                    # where the battle could have been underway
                    self.__init__(character_name, monster_name)

        except KeyError:
            print('{!s} does not exist. Please ensure the spelling/capitalization is '
                  'correct or reference the monster list'.format(monster_name))
            main_menu()

    @staticmethod
    # prompt for a predefined aggro level or enter a custom one
    def attack_aggressiveness():
        print('Attack with what level of aggressiveness?')
        print('1) Safe - 75% health')
        print('2) Balanced - 50% health')
        print('3) Aggressive - 25% health')
        print('4) Fight to the death!')
        print('5) Custom - DM entered')

        # do an input check
        try:
            while True:
                aggro_input = int(input())
                if aggro_input < 1 or aggro_input > 5:
                    print('Enter a number between 1 and 4')
                else:
                    break

            aggro = {1: .75, 2: .50, 3: .25, 4: 0}

            if aggro_input == 5:
                custom_aggro = float(input('Enter a health percentage \n'))
                aggro[aggro_input] = custom_aggro / 100

            print('Battle will stop when the character reaches {!s}% of their starting health \n'.format(aggro[aggro_input]))

            return aggro[aggro_input]

        except ValueError:
            print('Enter an aggressiveness option')
            Battle.attack_aggressiveness()

        except SyntaxError:
            Battle.attack_aggressiveness()

    @staticmethod
    def damage_modifier():
        print('Use which attack modifier?')
        print('1) Strength')
        print('2) Dexterity')

        damage_modifiers = {1: "strModifier", 2: "dexModifier"}
        while True:
            try:
                modifier_selection = int(input())
                if modifier_selection > 2:
                    raise ValueError

                print('Damage modifier is set to: {!s} \n\n'.format(damage_modifiers[modifier_selection]))
                return damage_modifiers[modifier_selection]

            except ValueError:
                print('Enter a valid number')
                Battle.damage_modifier()

    def do_character_attack(self, damage_type, char_hit_roll):
        # refresh character/monster profiles so we dont have to reload them manually
        self.__init__(self.character_name, self.monster_name)

        try:
            if char_hit_roll < 20:
                # compare if roll stats are greater than character's armor, subtract damage from players health
                # perform health check and display new values
                char_attack_hit = char_hit_roll + self.char['attackHit'] + self.char['proficiency']
                if char_attack_hit > self.mons['armorClass']:
                    print('Character attack roll: {!s}'.format(char_attack_hit))

                    # calculate attack damage
                    damage_roll = random.randint(1, self.char['damageDice']) + self.char[damage_type]
                    print('{!s} hit {!s} for {!s} damage'.format(self.character_name, self.monster_name, damage_roll))
                    new_mons_health = self.mons['hitPoints'] - damage_roll
                    # failed it
                else:
                    print('{!s} did not hit above {!s}\'s armor class! \n'.format(self.character_name, self.monster_name))

            elif char_hit_roll == 20:
                print('***CRITICAL DAMAGE ROLL***')
                crit_damage_roll = (self.char['damageDice'] * 2) + self.char[damage_type]
                print('Critical damage roll hit for: {!s}'.format(crit_damage_roll))
                # calculate health impacts of monster
                new_mons_health = self.mons['hitPoints'] - crit_damage_roll

            Monsters.change_stat(Monsters(), self.monster_name, 'hitPoints', new_mons_health)

        # if KeyError, a stat is missing from a profile somewhere
        except KeyError as ker:
            print('A character stat seems to be missing.')
            print(ker)
            main_menu()

    # perform single monster attack
    def do_monster_attack(self, aggro_level):
        # refresh character/monster profiles so we dont have to reload them manually
        self.__init__(self.character_name, self.monster_name)

        # roll d20
        random.seed()
        mons_hit_roll = random.randint(1, 20)

        # attacks are done here
        try:
            # compare if roll stats are greater than self.character's armor, subtract damage from players health
            # perform health check and display new values
            monster_attack_hit = mons_hit_roll + self.mons['attackHit']
            if monster_attack_hit > self.char['armorClass']:
                print('Monster attack roll: {!s}'.format(monster_attack_hit))
                attack_roll = random.randint(1, self.mons['damageDice'])
                print('{!s} hit {!s} for {!s} damage'.format(self.monster_name, self.character_name, attack_roll))

                # calculate health impacts and aggro level health
                new_char_health = self.char['hitPoints'] - attack_roll
                Characters.change_stat(Characters(), self.character_name, 'hitPoints', new_char_health)

                if (self.char['hitPoints'] - (self.char['hitPoints'] * aggro_level)) == new_char_health:
                    print('Character\'s desired aggro level health reached! \n')
                    main_menu()

            # failed it
            else:
                print('{!s} did not hit above {!s}\'s armor class! \n'.format(self.monster_name, self.character_name))

        # if KeyError, a stat is missing from a profile somewhere
        except KeyError as ker:
            print('A monster stat seems to be missing.')
            print(ker)
            main_menu()

    # prompt/perform a health reset of the monster for next time
    def reset_monster_health(self):
        print('Do you want to reset {!s}\'s health to default?'.format(self.monster_name))
        while True:
            yes_no = input('Enter "y" or "n"  \n')  # we prompt for n but do nothing below if its entered since that's moot
            if yes_no == 'y':
                default_hp = self.mons['defaultHP']
                Monsters.change_stat(Monsters(), self.monster_name, 'hitPoints', default_hp)
                break

            elif yes_no == 'n':
                break

            else:
                continue
