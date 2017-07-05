import pickle


diacritic_signs = 'ాిీుూృౄెేైొోౌఁంః '
virama = '్'
vowels = 'అఆఇఈఉఊఋఌఎఏఐఒఓఔ'
consonants = 'కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ'
others = 'ఽౘౙౠౡౢౣ'
numerals = '౦౧౨౩౪౫౬౭౮౯'

symbols = {
    'diacritic_signs': diacritic_signs,
    'virama': virama,
    'vowels': vowels,
    'consonants': consonants,
    'others': others,
}

all_symbols = ''.join(symbols.values())


def symbol_type(symbol):
    for key, value in symbols.items():
        if symbol in value:
            return key
    print(symbol)


with open('words_counter.pkl', 'rb') as fh:
    words_counter = pickle.load(fh)
all_words = set(words_counter.keys())


def probability(word):
    N = sum(words_counter.values())
    return words_counter[word] / N


with open('wrong_words.txt') as fh:
    wrong_words = [i.strip() for i in fh.readlines()]


def syllables(word):
    splits = []
    for char in word:
        try:
            if splits[-1][-1] == virama:
                splits[-1] = splits[-1] + char
                continue
        except IndexError:
            pass
        if char in diacritic_signs or char == virama:
            splits[-1] = splits[-1] + char
        else:
            splits.append(char)

    return splits


def get_edits(word, distance=1):
    if distance == 1:
        edits = edits1(word)
    return set(edits)


def edits1(word):
    "All edits that are one edit away from `word`."
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in all_symbols]
    inserts = [L + c + R for L, R in splits for c in all_symbols]
    combinations = deletes + transposes + inserts + replaces
    return combinations


def edits2(syllable):
    symbols = list(syllable)
    symbol_types = [symbol_type(s) for s in symbols]
    combinations = []
    return combinations


def get_words(syllables, index, edits):
    _words = []
    for edit in edits:
        new_syllables = syllables.copy()
        new_syllables[index] = edit
        new_word = ''.join(new_syllables)
        _words.append(new_word)
    return _words


def suggestions(word):
    combinations = []
    _syllables = syllables(word)
    for index, syllable in enumerate(_syllables):
        edits = get_edits(syllable)
        words = get_words(_syllables, index, edits)
        combinations.extend(words)
    matches = {s for s in combinations if s in all_words}
    return matches


def correction(word):
    return max(suggestions(word), key=probability)


for word in wrong_words:
    print(word, correction(word), suggestions(word))
