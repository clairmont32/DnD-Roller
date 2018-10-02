import os
import json
import random


class Characters:

	def __init__(self):
		cwd = os.getcwd()
		if os.path.exists('characters.json') is False:
			print('Could not find characters.json in '.format(cwd))

		if os.path.exists('monsters.json') is False:
			print('Could not find monsters.json in '.format(cwd))

		with open('Characters.json', 'r') as characters_file:
			self.characters = json.load(characters_file)

	def create_character(self, name):
		self.characters[name] = {}

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))

	def remove_character(self, name):
		del self.characters[name]

		with open('characters.json', 'w') as characters_file:
			characters_file.truncate(0)
			characters_file.write(json.dumps(self.characters))
