import heretic_functions

def remove_heretic(components):
	response = ''
	match = heretic_functions.non_heretic_pattern.search(components['arguments'])
	if match:
		target = match.groups()[0]
		if not components['sender'] == target:
			heretic_functions.build_heretics_db()
			heretic_functions.remove_heretic(target)
			response = 'noted'

	return response