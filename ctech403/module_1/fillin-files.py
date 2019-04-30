import random

# Placeholders
NOUN_PLACEHOLDER = '___NOUN___'
ADJECTIVE_PLACEHOLDER = '___ADJ___'
VERB_PLACEHOLDER = '___VERB___'

# Import word lists and story template
with open('nouns.txt') as f:
    nouns = f.read().splitlines()
with open('adjectives.txt') as f:
    adjectives = f.read().splitlines()
with open('verbs.txt') as f:
    verbs = f.read().splitlines()

with open('story.txt') as f:
    story = f.read()

# Returns a string with each instance of placeholder in text replaced by a
# random choice from word_list
def fill_in(text, placeholder, word_list):
    while placeholder in text:
        new_word = random.choice(word_list)
        text = text.replace(placeholder, new_word, 1)
    return text

# Perform substitutions for each list of words
story = fill_in(story, NOUN_PLACEHOLDER, nouns)
story = fill_in(story, ADJECTIVE_PLACEHOLDER, adjectives)
story = fill_in(story, VERB_PLACEHOLDER, verbs)

# Output story with substitutions
print(story)
