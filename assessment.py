"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    words_in_phrase = phrase.split(" ")
    unique_words_in_string = {}

    for word in words_in_phrase:
        unique_words_in_string[word] = unique_words_in_string.get(word, 0) + 1

    return unique_words_in_string


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    name_and_price_dict = {"Watermelon": 2.95,
                           "Cantaloupe": 2.50,
                           "Musk": 3.25,
                           "Christmas": 14.25,
                           }

    return name_and_price_dict.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    word_lengths_and_words = {}
    for word in words:
        word_lengths_and_words[len(word)] = word_lengths_and_words.get(len(word), [])
        word_lengths_and_words[len(word)].append(word)
        word_lengths_and_words[len(word)].sort()

    word_lengths = word_lengths_and_words.keys()
    word_lengths.sort()
    master_list = []

    for lengths in word_lengths:

        master_list.append((lengths, word_lengths_and_words[lengths]))

    return master_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_to_pirate = {
                        'sir': 'matey',
                        'hotel': 'fleabag inn',
                        'student': 'swabbie',
                        'man': 'matey',
                        'professor': 'foul blaggart',
                        'restaurant': 'galley',
                        'your': 'yer',
                        'excuse': 'arr',
                        'students': 'swabbies',
                        'are': 'be',
                        'restroom': 'head',
                        'my': 'me',
                        'is': 'be'
                        }

    sentence_to_words = phrase.split(" ")
    for index in range(0, len(sentence_to_words)):
        sentence_to_words[index] = english_to_pirate.get(sentence_to_words[index], sentence_to_words[index])

    return " ".join(sentence_to_words)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    next_word_options = {}
    for name in names:
        next_word_options[name[0]] = next_word_options.get(name[0], [])
        next_word_options[name[0]].append(name)

    result = []
    
    current_word = names[0]
    next_word_first_letter = current_word[-1:]
    words_of_a_letter = next_word_options.get(next_word_first_letter, [])

    result.append(current_word)
    next_word_options[current_word[0]].remove(current_word)

    while words_of_a_letter != []:
        current_word = words_of_a_letter[0]
        next_word_first_letter = current_word[-1:]

        result.append(current_word)
        next_word_options[current_word[0]].remove(current_word)
        
        words_of_a_letter = next_word_options.get(next_word_first_letter, [])
        
# as words_of_a_letter

    return result

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
