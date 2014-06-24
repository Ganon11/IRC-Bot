from config import cmd_char
import heretic_functions

CMD_STRING = cmd_char + 'heretic ' # Note the trailing space!

def heretic(components):
	response = ''
	target = ''
	try:
		target = components['arguments'].split(CMD_STRING)[1]
	except:
		target = components['sender']
	count = heretic_functions.get_heretic(target)
	response = '%(target)s (%(count)s denunciation%(plural)s)' % { 'target': target, 'count': count, 'plural': '' if count == 1 else 's'}
	return response.encode('utf8')

if __name__ == '__main__':
	comp = { 'arguments': cmd_char + 'heretic', 'sender': 'mstark' }
	print heretic(comp)