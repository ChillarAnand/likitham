"""
Script to download telugu wikipedia dump, extract text from it
and build a corpus.
"""

import pickle
import sys
import textwrap
from collections import Counter

from utils import get_syllables

wiki_dump_url = 'https://dumps.wikimedia.org/tewiki/20170701/tewiki-20170701-pages-articles-multistream.xml.bz2'


def clean_word(word):
    return word.strip('".,!?; \n\t()[]')


def save_text(text, file_name):
    with open(file_name, 'w') as fh:
        for line in text:
            fh.write(line)
            fh.write('\n')


def save_counter(counter, file_name):
    with open(file_name, 'w') as fh:
        for word, freq in counter.most_common():
            line = "{} {}\n".format(word, freq)
            fh.write(line)


def save_object(obj, file_name):
    with open(file_name, 'wb') as fh:
        pickle.dump(obj, fh)


def is_english(word):
    try:
        word.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False


if len(sys.argv) > 1:
    wiki_dump_file = sys.argv[1]
else:
    wiki_dump_file = 'tewiki.txt'
    wiki_dump_file = 'test_wiki.txt'


print('Reading data from dump file: {}'.format(wiki_dump_file))
with open(wiki_dump_file) as fh:
    # data = fh.read()
    # lines = data.split('\n')

    lines = fh.readlines()


lines = [line for line in lines if not line.startswith(('<doc', '</doc>'))]
book_data = ' '.join(lines)
book = textwrap.fill(book_data, width=80)

book_file = 'book.txt'
with open(book_file, 'w') as fh:
    fh.write(book)
print('Writing book to {}'.format(book_file))
del book, book_data

sys.exit()

words = data.split()
words = [clean_word(word) for word in words if not is_english(word)]
save_text(words, 'words.txt')

words_counter = Counter(words)
save_object(words_counter, 'words_counter.pkl')
del words_counter


syllables = []

for word in words:
    syllables.extend(get_syllables(word))

syllables_counter = Counter(syllables)


save_counter(syllables_counter, 'syllables_counter.txt')
