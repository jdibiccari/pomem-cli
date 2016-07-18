
import re
import random
from slugify import slugify
from string import punctuation as PUNCTUATION
import yaml
import nltk

POS = ['NN+', 'VB+', 'JJ+', 'RB+']
DIFFICULTY_LEVELS = [1, 2, 3, 4, 5]
BLEEP_CHARACTER = "."
POEM_DIR = 'data/'

def load_yaml_from_file(input):
    file = 'data/{input}.yml'.format(input=input)
    with open (file, 'r') as f:
        doc = yaml.load(f)
        poem = doc['body'].splitlines(True)
        return poem

def tokens(line):
    return nltk.word_tokenize(line)

def tagged_tokens(tokens):
    return nltk.pos_tag(tokens)

def pos_filter(tagged_tokens):
    pos_reg = '|'.join(POS)
    match_words = []
    nonmatch_words = []
    for token in tagged_tokens:
        if re.match(pos_reg, token[1]):
            match_words.append(token[0])
        else:
            if not token[0] in PUNCTUATION:
                nonmatch_words.append(token[0])
    return [match_words, nonmatch_words]

def pos_tag_line(line):
    return pos_filter(tagged_tokens(tokens(line)))

def select_random_from_list(removal_candidates, qty=1):
    high_priority_words = removal_candidates[0]
    low_priority_words = removal_candidates[1]

    random.shuffle(high_priority_words)
    random.shuffle(low_priority_words)

    all_words = high_priority_words + low_priority_words
    print all_words
    return all_words[:qty]

# def select_random_from_list(removal_candidates, qty=1):
#     selection = []
#     match_words = removal_candidates[0]
#     match_max = len(match_words)
#     nonmatch_words = removal_candidates[1]
#     nonmatch_max = len(nonmatch_words)
#     remainder = qty - match_max
#     if remainder > 0:
#         selection = random.sample(match_words, match_max)
#         if remainder > nonmatch_max:
#             selection += random.sample(nonmatch_words, nonmatch_max)
#         else:
#             selection += random.sample(nonmatch_words, remainder)
#     else:
#         selection = random.sample(match_words, qty)
#     return selection

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


