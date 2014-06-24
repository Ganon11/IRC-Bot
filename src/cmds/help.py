import config

CMD_STRING = config.cmd_char + 'help'

def help(components): # !help
   '''Returns a string containing all the available commands'''

   response = ''

   if components['arguments'] == CMD_STRING:
      # the user sent just the command, no garbage
      response = (str(len(config.cmds['user'] + config.cmds['core'])) + ' available commands (user) ')

      for command in sorted(config.cmds['user']):
         response = response + command + ' '
            
      response = response + '(core) '
      for command in sorted(config.cmds['core']):
         response = response + command + ' '

   return response.encode('utf8')
