import honor_functions

def honour(components):
    phrase = components['arguments'].split('!honour ')[1]
    if honor_functions.check_honor(phrase):
        response = phrase + " has honour."
    else
        response = phrase + " is without honour."
    return response.encode('utf8')