
import re
import random
from slugify import slugify
from string import punctuation as PUNCTUATION
import yaml
import nltk

# Weight parts of speech so higher probablity of removing some than others
# Or keep as is and only remove words not tagged as below if there is nothing else to remove
POS = ['NN+', 'VB+', 'JJ+', 'RB+']
DIFFICULTY_LEVELS = [1]
BLEEP_CHARACTER = "."
POEM_DIR = 'data/'

## NEW ##
def load_yaml_from_file(input):
    file = 'data/{input}.yml'.format(input=input)
    with open (file, 'r') as f:
        doc = yaml.load(f)
        poem = doc['body'].splitlines(True)
        return poem

# def load_poem_from_file(input):
#     with open (input, "r") as file:
#         lines = list(file)
#     return lines

def tokens(line):
    return nltk.word_tokenize(line)

def tagged_tokens(tokens):
    return nltk.pos_tag(tokens)

# def pos_filter(tagged_tokens):
#     pos_reg = '|'.join(POS)
#     return [ token[0] for token in tagged_tokens if re.match(pos_reg, token[1])]

def pos_filter(tagged_tokens):
    pos_reg = '|'.join(POS)
    match_words = []
    nonmatch_words = []
    print tagged_tokens
    for token in tagged_tokens:
        if re.match(pos_reg, token[1]):
            match_words.append(token[0])
        else:
            if not token[0] in PUNCTUATION:
                nonmatch_words.append(token[0])
    return [match_words, nonmatch_words]

def pos_tag_line(line):
    return pos_filter(tagged_tokens(tokens(line)))

# def select_random_from_list(removal_candidates, qty=1):
#     selection = []
#     max_selection = len(removal_candidates)
#     try:
#         selection = random.sample(removal_candidates, qty)
#     except ValueError as e:
#         selection = random.sample(removal_candidates, max_selection)
#     return selection

def select_random_from_list(removal_candidates, qty=1):
    selection = []
    match_words = removal_candidates[0]
    match_max = len(match_words)
    nonmatch_words = removal_candidates[1]
    nonmatch_max = len(nonmatch_words) # 1

    # If qty is greater than the max selection
    # Select as many as possible from match words

    remainder = qty - match_max # 1 - 3 = -2 or 2 - 1 = 1 or 1 - 0 = 1 or 1 - 1 = 0
    print "qty - match_max = remainder"
    print qty, match_max, remainder
    if remainder > 0:
        selection = random.sample(match_words, match_max)
        print "first selection: {}".format(selection)
        print "remainder | nonmatch_max"
        print remainder, nonmatch_max
        if remainder > nonmatch_max:
            selection += random.sample(nonmatch_words, nonmatch_max)
            print "second selection: {}".format(selection)
        else:
            selection += random.sample(nonmatch_words, remainder)
            print "second selection: {}".format(selection)
    else:
        selection = random.sample(match_words, qty)
        print "first selection: {}".format(selection)
    return selection


def bleep_line(line, level=1, bleep_character=BLEEP_CHARACTER):
    pos_tokens = pos_tag_line(line)
    to_remove = select_random_from_list(pos_tokens, level)
    new_line = line
    for word in to_remove:
        replacement = bleep_character * len(word)
        new_line = new_line.replace(word, replacement, 1)
    return new_line

def bleep(lines, level=1, bleep_character=BLEEP_CHARACTER):
    # Per each line there is a set number of possibilites, could store eventually.
    return [bleep_line(line, level, bleep_character) for line in lines]


