import heretic_functions

def heretics(components):
	heretic_functions.build_heretics_db()
	response = ''
	count = 5
	try:
		count = int(components['arguments'].split('!heretics ')[1])
	except:
		pass
	return heretic_functions.get_heretics(count).encode('utf8')
