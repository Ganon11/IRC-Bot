import heretic_functions

def add_heretic(components):
	heretic_functions.build_heretics_db();
	response = ''
    match = heretic_functions.heretic_pattern.search(components['arguments'])
    if match:
    	heretic_functions.add_heretic(match.groups()[0])
    	response = 'noted'

    return response