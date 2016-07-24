import os
import yaml
from bleeping import POEM_DIR

def list_poems():
	library = os.listdir(POEM_DIR)
	for file in library:
		with open (POEM_DIR + file, 'r') as f:
			doc = yaml.load(f)
			print "{} By: {}".format(doc['title'], doc['author'])
