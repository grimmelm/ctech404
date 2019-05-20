import random

# Story template
story = 'Yesterday, I ___VERB___ to the store to buy a ___NOUN___. But on my way, I ran into a ___ADJ___ ___NOUN___. I was very ___ADJ___. Then I remembered that I had a ___NOUN___ in my pocket. I ___VERB___ behind a ___ADJ___ ___NOUN___.'

# Placeholders
NOUN_PLACEHOLDER = '___NOUN___'
ADJECTIVE_PLACEHOLDER = '___ADJ___'
VERB_PLACEHOLDER = '___VERB___'

# Word lists
NOUNS = ['cat', 'dog', 'zeppelin', 'boomerang', 'trombone']
ADJECTIVES = ['red', 'hunormous', 'intricate', 'merciless']
VERBS = ['vomited', 'catapulted', 'squeaked']

# Returns a string with each instance of placeholder in text replaced by a
# random choice from word_list
def fill_in(text, placeholder, word_list):
    while placeholder in text:
        new_word = random.choice(word_list)
        text = text.replace(placeholder, new_word, 1)
    return text

# Perform substitutions for each list of words
story = fill_in(story, NOUN_PLACEHOLDER, NOUNS)
story = fill_in(story, ADJECTIVE_PLACEHOLDER, ADJECTIVES)
story = fill_in(story, VERB_PLACEHOLDER, VERBS)

# Output story with substitutions
print(story)
