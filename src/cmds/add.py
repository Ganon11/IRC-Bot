import config
import honor_functions
from functions import is_registered

def add(socket, components):
    if not components['sender'] in config.owner or not is_registered(socket, components['sender']):
        return 'This command can be run only by the owners!'.encode('utf8')
    arguments = components['arguments'].split('!add ')[1].split(':')
    phrase = arguments[0]
    lower_phrase = phrase.lower()
    value = arguments[1].lower()
    
    truth_value = False
    if value == 'honorable' or value == 'honourable':
        truth_value = True
        
    phrases = honor_functions.load_phrases()
    phrases[lower_phrase] = truth_value
    honor_functions.save_phrases(phrases)
    response = "'%s' added as '%s'" % (phrase, value)
    return response.encode('utf8')