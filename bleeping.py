import re
import random
from slugify import slugify
from string import punctuation as PUNCTUATION
import yaml
import nltk
from nltk.corpus import wordnet as wn

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
    import itertools
    for word_set in removal_candidates:
        random.shuffle(word_set)

    return list(itertools.chain.from_iterable(removal_candidates))[:qty]

# def get_choices(words):
#     output = ''
#     for i, word in enumerate(words):
#         output += '{0}. {1} '.format(i + 1, word)
#     return output

def get_similar_words(word):
    output = [word]
    for ss in wn.synsets(word):
        for lemma in ss.lemma_names():
            output.append(lemma)
    return output


def bleep_line(line, level=1, bleep_character=BLEEP_CHARACTER):
    pos_tokens = pos_tag_line(line)
    to_remove = select_random_from_list(pos_tokens, level)
    new_line = line
    for word in to_remove:
        replacement = bleep_character * len(word)
        new_line = new_line.replace(word, replacement, 1)
    return new_line, to_remove

def bleep(lines, level=1, bleep_character=BLEEP_CHARACTER):
    # Per each line there is a set number of possibilites, could store eventually.
    return [bleep_line(line, level, bleep_character) for line in lines]




