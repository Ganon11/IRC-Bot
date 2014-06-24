from config import cmd_char
import honor_functions

CMD_STRING = cmd_char + 'honour ' # Note the trailing space!
USAGE_STRING = 'Usage: %shonour <phrase>'

def honour(components):
	args = components['arguments'].split(CMD_STRING)
	if len(args) == 1:
		return USAGE_STRING
    phrase = args[1]
    if honor_functions.check_honor(phrase):
        response = phrase + " has honour."
    else:
        response = phrase + " is without honour."
    return response.encode('utf8')