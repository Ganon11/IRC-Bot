import heretic_functions

def remove_heretic(components):
	heretic_functions.build_heretics_db();
	response = ''
	match = heretic_functions.non_heretic_pattern.search(components['arguments'])
	if match:
		heretic_functions.remove_heretic(match.groups()[0])
		response = 'noted'

	return response