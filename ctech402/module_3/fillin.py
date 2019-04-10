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

# Perform substitutions
while NOUN_PLACEHOLDER in story:
    new_word = random.choice(NOUNS)
    story = story.replace(NOUN_PLACEHOLDER, new_word, 1)
while ADJECTIVE_PLACEHOLDER in story:
    new_word = random.choice(ADJECTIVES)
    story = story.replace(ADJECTIVE_PLACEHOLDER, new_word, 1)
while VERB_PLACEHOLDER in story:
    new_word = random.choice(VERBS)
    story = story.replace(VERB_PLACEHOLDER, new_word, 1)

# Output story with substitutions
print(story)
