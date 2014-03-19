import hashlib
import os

def load_phrases():
    honor_file = open(os.path.join(os.getcwd(), '..', 'files', 'honorable_phrases.txt'))
    phrases = dict()
    for line in honor_file:
        line = line.strip()
        pos = line.find(':')
        file_phrase = line[:pos].lower()
        honorable = line[pos + 1:]
        is_honorable = False
        if honorable == 'Honorable':
            is_honorable = True
        phrases[file_phrase] = is_honorable
    return phrases

def check_honor(phrase):
    lower_phrase = phrase.lower()
    phrases = load_phrases()
    if lower_phrase in phrases:
        if phrases[lower_phrase]:
            return True
        else:
            return False
    else:
        hasher = hashlib.md5()
        hasher.update(phrase)
        last_digit = hasher.hexdigest()[-1]
        if last_digit in ['0', '1', '2', '3', '4', '5', '6', '7']:
            return True
        else:
            return False
    return response