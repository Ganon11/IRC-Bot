import heretic_functions

def remove_heretic(components):
	response = ''
	match = heretic_functions.singular_non_heretic_pattern.search(components['arguments'])
	if match:
		target = match.groups()[0]
		if not components['sender'] == target:
			heretic_functions.build_heretics_db()
			heretic_functions.change_heretic(components['sender'], target, -1)
			response = 'noted'
	else:
		match = heretic_functions.plural_non_heretic_pattern.search(components['arguments'])
		if match:
			target = match.groups()[0]
			if not components['sender'] == target:
				heretic_functions.build_heretics_db()
				heretic_functions.change_heretic(components['sender'], target, -1)
				response = 'noted'

	return response