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

# These are the new ones that James verbalizes as potential added sections
while ADVERB_PLACEHOLDER in story:
    new_word = random.choice(ADVERBS)
    story = story.replace(ADVERB_PLACEHOLDER, new_word, 1)
while EXCLAMATION_PLACEHOLDER in story:
    new_word = random.choice(EXCLAMATIONS)
    story = story.replace(EXCLAMATION_PLACEHOLDER, new_word, 1)
while PLACE_PLACEHOLDER in story:
    new_word = random.choice(PLACES)
    story = story.replace(PLACE_PLACEHOLDER, new_word, 1)
