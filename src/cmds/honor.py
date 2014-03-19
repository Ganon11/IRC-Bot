import honor_functions

def honor(components):
    phrase = components['arguments'].split('!honor ')[1]
    if honor_functions.check_honor(phrase):
        response = phrase + " has honor."
    else:
        response = phrase + " is without honor."
    return response.encode('utf8')