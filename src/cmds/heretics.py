from config import cmd_char
import heretic_functions

CMD_STRING = cmd_char + 'heretics ' # Note the trailing space!

def heretics(components):
	heretic_functions.build_heretics_db()
	response = ''
	count = 5
	try:
		count = int(components['arguments'].split(CMD_STRING)[1])
	except:
		pass
	return heretic_functions.get_heretics(count).encode('utf8')
