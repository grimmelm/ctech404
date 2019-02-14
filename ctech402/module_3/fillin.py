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
    newWord = random.choice(NOUNS)
    story = story.replace(NOUN_PLACEHOLDER, newWord, 1)
while ADJECTIVE_PLACEHOLDER in story:
    newWord = random.choice(ADJECTIVES)
    story = story.replace(ADJECTIVE_PLACEHOLDER, newWord, 1)
while VERB_PLACEHOLDER in story:
    newWord = random.choice(verbs)
    story = story.replace(VERB_PLACEHOLDER, newWord, 1)

# Output story with substitutions
print(story)
