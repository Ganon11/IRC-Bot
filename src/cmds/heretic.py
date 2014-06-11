import heretic_functions

def heretic(components):
	response = ''
	target = components['arguments'].split('!heretic ')[1]
	count = heretic_functions.get_heretic(target)
	response = '%(target)s (%(count)s denunciation%(plural)s)' % { 'target': target, 'count': count, 'plural': '' if count == 1 else 's'}
	return response.encode('utf8')

if __name__ == '__main__':
	comp = { 'arguments': '!heretic aletheia' }
	print heretic(comp)