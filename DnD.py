import os
import json
import random


# means of interacting with characters in characters.json
class Characters:
	def __init__(self):
		cwd = os.getcwd()
		if os.path.exists('characters.json') is False:
			exit(print('Could not find characters.json in '.format(cwd)))

		with open('Characters.json', 'r') as characters_file:
			self.characters = json.load(characters_file)

	# creates an empty character in characters.json
	def create_character(self, name):
		self.characters[name] = {}

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))

		return

	# removes a character from characters.json
	def remove_character(self, name):
		try:
			del self.characters[name]
			with open('characters.json', 'w') as characters_file:
				characters_file.truncate(0)
				characters_file.write(json.dumps(self.characters))

		except KeyError:
			print('{!s} does not have a character profile saved!'.format(name))

		return

	# lists current character names
	def list_characters(self):
		names = [name for name in self.characters.keys()]
		for name in names:
			print(name)

	# prompt for character stats
	def add_stats(self):
		name = str(input('Enter character name: \n'))
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
		self.characters[name] = {"armorClass": armor_class, "initiative": initiative, "hitPoints": hit_points,
		                         "attackHit": attack_hit, "damageDice": damage_dice, "strModifier": str_modifier,
								 "dexModifier": dex_modifier, "cure": cure, "numAttacks": num_attacks,
								 "proficiency": proficiency
								 }

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))

	# lists stats for a given character
	def list_stats(self, name):
		try:
			for stat in self.characters[name].keys():
				print(stat)
		except KeyError:
			print('{!s} does not have a character profile saved!'.format(name))

		return

	# updates a current stat
	def change_stat(self, name, stat, new_stat):
		try:
			self.characters[name].update({stat: new_stat})
		except KeyError as ker:
			print('Could not update {!s}'.format(new_stat))
			print(ker)

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))


# means of interacting with monsters in monsters.json
class Monsters:
	def __init__(self):
		cwd = os.getcwd()

		if os.path.exists('monsters.json') is False:
			exit(print('Could not find monsters.json in '.format(cwd)))

		with open('monsters.json', 'r') as monsters_file:
			self.monsters = json.load(monsters_file)

	# creates an empty monster in monsters.json
	def create_monster(self, name):
		self.monsters[name] = {}

		with open('monsters.json', 'w') as monsters_file:
			monsters_file.truncate(0)
			monsters_file.write(json.dumps(self.monsters))

		return

	# removes a monster from monsters.json
	def remove_monster(self, name):
		try:
			del self.monsters[name]
			with open('monsters.json', 'w') as monsters_file:
				monsters_file.truncate(0)
				monsters_file.write(json.dumps(self.monsters))

		except KeyError:
			print('{!s} does not have a monster profile saved!'.format(name))

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
	def list_stats(self, name):
		try:
			for stat in self.monsters[name].keys():
				print(stat)
		except KeyError:
			print('{!s} does not have a monster profile saved!'.format(name))

		return

	# updates a current stat
	def change_stat(self, name, stat, new_stat):
		try:
			self.monsters[name].update({stat: new_stat})
		except KeyError as ker:
			print('Could not update {!s}'.format(new_stat))
			print(ker)

		with open('monsters.json', 'w') as monsters_file:
			monsters_file.truncate(0)
			monsters_file.write(json.dumps(self.monsters))

