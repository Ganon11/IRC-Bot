import honor_functions

def add(components):
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
    response = "'" + phrase + "' added as '" + str(truth_value) + "'"
    return response.encode('utf8')