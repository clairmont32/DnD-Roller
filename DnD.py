import os
import json
import random


# means of interacting with characters in characters.json
class Characters:

	def __init__(self):
		cwd = os.getcwd()
		if os.path.exists('characters.json') is False:
			exit(print('Could not find characters.json in '.format(cwd)))

		if os.path.exists('monsters.json') is False:
			exit(print('Could not find monsters.json in '.format(cwd)))

		with open('Characters.json', 'r') as characters_file:
			self.characters = json.load(characters_file)

	def create_character(self, name):
		self.characters[name] = {}

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))

		return

	def remove_character(self, name):
		try:
			del self.characters[name]
			with open('characters.json', 'w') as characters_file:
				characters_file.truncate(0)
				characters_file.write(json.dumps(self.characters))

		except KeyError:
			print('{!s} does not have a character profile saved!'.format(name))

		return

	def list_characters(self):
		names = [name for name in self.characters.keys()]
		for name in names:
			print(name)

	def add_stats(self):
		while True:
			try:
				num_stats = int(input('How many stats do you want to add? \n'))
				break
			except ValueError:
				print('Enter a number.')

		name = input('Name of character to add stats to: \n')

		while num_stats > 0:
			stat_name = input('Name of stat: \n')
			stat_value = input('Value of stat: \n')
			if stat_value.isdigit is False:
				print('Enter a number for the stat value.')
			else:
				self.characters[name].updatae({stat_name: stat_value})
				num_stats -= 1

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))

	def list_stats(self, name):
		try:
			for stat in self.characters[name].keys():
				print(stat)
		except KeyError:
			print('{!s} does not have a character profile saved!'.format(name))

		return

	def change_stat(self, name, stat, new_stat):
		try:
			self.characters[name].update({stat: new_stat})
		except KeyError as ker:
			print('Could not update {!s}'.format(new_stat))
			print(ker)

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))


