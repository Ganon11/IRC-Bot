import hashlib
import os

def honor(components):
    phrase = components['arguments'].split('!honor ')[1]
    lower_phrase = phrase.lower()
    
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
    
    if lower_phrase in phrases:
        if phrases[lower_phrase]:
            response = phrase + " has honor."
        else:
            response = phrase + " is without honor."
    else:
        hasher = hashlib.md5()
        hasher.update(phrase)
        last_digit = hasher.hexdigest()[-1]
        if last_digit in ['0', '1', '2', '3', '4', '5', '6', '7']:
            response = phrase + " has honor."
        else:
            response = phrase + " is without honor."
    return response