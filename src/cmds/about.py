def about(components): # !about
    '''Returns a string containing info about the bot'''
    response = ''

    if components['arguments'] == '!about':
        # the user sent just the command, no garbage
<<<<<<< HEAD
        response = 'Author: Paullik @ http://github.com/paullik'
=======
        response = "Author: Paullik @ http://github.com/paullik, Modified by: Ganon11 @ http://github.com/Ganon11"
>>>>>>> upstream/WorfBot

    return response.encode('utf8')
