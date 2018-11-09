#!/usr/bin/python3
import os
import json
import random


# means of interacting with characters in characters.json
class Characters:
	def __init__(self):
		cwd = os.getcwd()
		if os.path.exists('characters.json') is False:
			exit(print('Could not find characters.json in '.format(cwd)))

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

		except KeyError:
			print('{!s} does not have a character profile saved!'.format(character_name))

		return

	# lists current character names
	def list_characters(self, character_name):
		names = [name for name in self.characters.keys()]
		for name in names:
			print(name)

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
		                         "attackHit": attack_hit, "damageDice": damage_dice, "strModifier": str_modifier,
								 "dexModifier": dex_modifier, "cure": cure, "numAttacks": num_attacks,
								 "proficiency": proficiency
								 }

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))
       
		print('\n')
		print('Stats added. \n\n')

	# lists stats for a given character
	def list_stats(self, character_name):
		try:
			for stat in self.characters[character_name].keys():
				print(stat)
		except KeyError:
			print('{!s} does not have a character profile saved!'.format(self.character_name))

		return

	# updates a current stat
	def change_stat(self, character_name, stat, new_stat):
		try:
			self.characters[character_name].update({stat: new_stat})
		except KeyError as ker:
			print('Could not update {!s}'.format(new_stat))
			print(ker)

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))


# means of interacting with monsters in monsters.json
class Monsters:
	def __init__(self, monster_name):
		cwd = os.getcwd()

		if os.path.exists('monsters.json') is False:
			exit(print('Could not find monsters.json in '.format(cwd)))

		with open('monsters.json', 'r') as monsters_file:
			self.monsters = json.load(monsters_file)

		self.monster_name = monster_name

	# creates an empty monster in monsters.json
	def create_monster(self):
		self.monsters[self.monster_name] = {}

		with open('monsters.json', 'w') as monsters_file:
			monsters_file.truncate(0)
			monsters_file.write(json.dumps(self.monsters))

		return

	# removes a monster from monsters.json
	def remove_monster(self):
		try:
			del self.monsters[self.monster_name]
			with open('monsters.json', 'w') as monsters_file:
				monsters_file.truncate(0)
				monsters_file.write(json.dumps(self.monsters))

		except KeyError:
			print('{!s} does not have a monster profile saved!'.format(self.monster_name))

		return

	# lists current monster names
	def list_monsters(self):
		names = [name for name in self.monsters.keys()]
		for name in names:
			print(name)

	# prompt for monster stats
	def add_stats(self):
		name = str(input('Enter monster name: \n'))
		print('Enter numeric values for the below stats- ')
		while True:
			try:
				armor_class = int(input('Enter armor class: \n'))
				initiative = int(input('Enter initiative: \n'))
				hit_points = int(input('Enter HP: \n'))
				attack_hit = int(input('Enter attack hit: \n'))
				damage_dice = int(input('Damage die roll (1dX): \n'))
				num_attacks = int(input('Enter number of attacks: \n'))

				break
			except ValueError:
				print('You didn\'t enter a number!')

		# add to json
		self.monsters[name] = {"armorClass": armor_class, "initiative": initiative, "hitPoints": hit_points,
		                         "attackHit": attack_hit, "damageDice": damage_dice, "numAttacks": num_attacks}

		with open('monsters.json', 'w') as monsters_file:
			monsters_file.truncate(0)
			monsters_file.write(json.dumps(self.monsters))

	# lists stats for a given monster
	def list_stats(self):
		try:
			for stat in self.monsters[self.monster_name].keys():
				print(stat)
		except KeyError:
			print('{!s} does not have a monster profile saved!'.format(self.monster_name))

		return

	# updates a current stat
	def change_stat(self, stat, new_stat):
		try:
			self.monsters[self.monster_name].update({stat: new_stat})
		except KeyError as ker:
			print('Could not update {!s}'.format(new_stat))
			print(ker)

		with open('monsters.json', 'w') as monsters_file:
			monsters_file.truncate(0)
			monsters_file.write(json.dumps(self.monsters))


class Battle:
	def __init__(self, character_name, monster_name):
		super(Characters)
		super(Monsters)
		self.character_name = character_name
		self.monster_name = monster_name
		with open('characters.json', 'r') as characters_file:
			characters = json.load(characters_file)
			self.char = characters[character_name]
		with open('monsters.json', 'r') as monsters_file:
			monsters = json.load(monsters_file)
			self.mons = monsters[monster_name]


	def attack_aggressiveness(self, character_name):
		# work in attack until health percentage
		pass

	def compare_initiative(self):
		char_initiative = self.char['initiative']
		mons_initiative = self.mons['initiative']

		if mons_initiative > char_initiative:
			self.do_monster_attack()
			self.do_character_attack()

		elif mons_initiative < char_initiative:
			self.do_character_attack()
			self.do_monster_attack()

		elif mons_initiative == char_initiative:
			self.do_character_attack()
			self.do_monster_attack()

	def do_character_attack(self):
		# roll d20
		char_hit_roll = random.randint(1, 20)

		if self.char['hitPoints'] <= 0:
			print('{!s} has been killed!'.format(self.character_name))
			return

		# compare if roll stats are greater than character's armor, subtract damage from players health
		# perform health check and display new values
		char_attack_hit = char_hit_roll + self.char['attackHit'] + self.char['proficiency']
		if char_attack_hit > self.mons['armorClass']:
			print('Character attack hit: {!s}'.format(char_attack_hit))
			#
			# ADD THE MODIFIER DAMAGE HERE
			attack_roll = random.randint(1, self.char['damageDice']) + self.char['damageBonus']  # ADD THE MODIFIER TYPE DAMAGE HERE
			print('{!s} hit {!s} for {!s} damage'.format(self.character_name, self.monster_name, attack_roll))
			new_char_health = self.mons['hitPoints'] - attack_roll
			Characters.change_stat(self.character_name, 'hitPoints', new_char_health)
			print('{!s} has {!s} HP left. \n'.format(self.monster_name, new_char_health))

		# failed it
		else:
			print('{!s} did not hit above {!s}\'s armor class!'.format(self.character_name, self.monster_name))

	# perform single monster attack
	def do_monster_attack(self):
		# roll d20
		mons_hit_roll = random.randint(1, 20)

		if self.mons['hitPoints'] <= 0:
			print('{!s} has been killed!'.format(self.monster_name))
			return

		# compare if roll stats are greater than self.character's armor, subtract damage from players health
		# perform health check and display new values
		monster_attack_hit = mons_hit_roll + self.mons['attackHit']
		if monster_attack_hit > self.char['armorClass']:
			print('self.monster attack hit: {!s}'.format(monster_attack_hit))
			attack_roll = random.randint(1, self.mons['damageDice'])
			print('{!s} hit {!s} for {!s} damage'.format(self.monster_name, self.character_name, attack_roll))
			new_char_health = self.char['hitPoints'] - attack_roll
			Monsters.change_stat(self.monster_name, 'hitPoints', new_char_health)
			print('{!s} has {!s} HP left. \n'.format(self.character_name, new_char_health))

		# failed it
		else:
			print('{!s} did not hit above {!s}\'s armor class!'.format(self.monster_name, self.character_name))
