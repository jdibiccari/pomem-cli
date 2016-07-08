# Multi-line input
import re
import random
import yaml
import sys
import nltk

POS = ['NN+', 'VB+', 'JJ+', 'RB+']
DIFFICULTY_LEVELS = [1]
BLEEP_CHARACTER = "_"

## NEW ##
def load_yaml_from_file(input):
    with open (input, 'r') as f:
        doc = yaml.load(f)
        poem = doc['body'].splitlines(True)
        return poem

def load_poem_from_file(input):
    with open (input, "r") as file:
        lines = list(file)
    return lines

def tokens(line):
    return nltk.word_tokenize(line)

def tagged_tokens(tokens):
    return nltk.pos_tag(tokens)

def pos_filter(tagged_tokens):
    pos_reg = '|'.join(POS)
    return [ token[0] for token in tagged_tokens if re.match(pos_reg, token[1])]

def pos_tag_line(line):
    return pos_filter(tagged_tokens(tokens(line)))

def select_random_from_list(list, qty=1):
    selection = []
    max_selection = len(list)
    try:
        selection = random.sample(list, qty)
    except ValueError as e:
        selection = random.sample(list, max_selection)
    return selection

def bleep_line(line, level=1):
    pos_tokens = pos_tag_line(line)
    to_remove = select_random_from_list(pos_tokens, level)
    new_line = line
    for word in to_remove:
        replacement = BLEEP_CHARACTER * len(word)
        new_line = new_line.replace(word, replacement, 1)
    return new_line

def bleep(lines, level=1):
    # Per each line there is a set number of possibilites, could store eventually.
    return [bleep_line(line, level) for line in lines]


if __name__ == '__main__':
    file = sys.argv[1]
    level = int(sys.argv[2])
    lines = load_yaml_from_file('data/'+file)
    for line in bleep(lines, level=level):
        print line

