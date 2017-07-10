diacritic_signs = 'ాిీుూృౄెేైొోౌఁంః'
virama = '్'
vowels = 'అఆఇఈఉఊఋఌఎఏఐఒఓఔ'
consonants = 'కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ'
others = 'ఽౘౙౠౡౢౣ'
numerals = '౦౧౨౩౪౫౬౭౮౯'


def get_syllables(word):
    splits = []
    for char in word:
        try:
            if splits[-1][-1] == virama:
                splits[-1] = splits[-1] + char
                continue
        except IndexError:
            pass
        if char in diacritic_signs or char == virama:
            if splits:
                splits[-1] = splits[-1] + char
            else:
                pass
                # print(word, splits)
        else:
            splits.append(char)

    return splits
