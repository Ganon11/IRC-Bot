import config
import honor_functions
from functions import is_registered

CMD_STRING = config.cmd_char + 'add ' # Note the trailing space!
USAGE_STRING = 'Usage: %sadd <term>:<Honorable or Dishonorable>' % config.cmd_char

def add(socket, components):

    if not components['sender'] in config.owner or not is_registered(socket, components['sender']):
        return 'This command can be run only by the owners!'.encode('utf8')
    args = components['arguments'].split(CMD_STRING)
    if len(args) == 1: # Couldn't find terms
        return USAGE_STRING
    terms = args[1].split(':')
    if len(terms) == 1: # Improper format
        return USAGE_STRING

    phrase = terms[0]
    lower_phrase = phrase.lower()
    value = terms[1].lower()
    
    truth_value = False
    if value == 'honorable' or value == 'honourable':
        truth_value = True
        
    phrases = honor_functions.load_phrases()
    phrases[lower_phrase] = truth_value
    honor_functions.save_phrases(phrases)
    response = "'%s' added as '%s'" % (phrase, value)
    return response.encode('utf8')
