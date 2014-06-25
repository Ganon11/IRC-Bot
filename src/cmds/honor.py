from config import cmd_char
import honor_functions

CMD_STRING = cmd_char + 'honor ' # Note the trailing space!
USAGE_STRING = 'Usage: %shonor <phrase>' % cmd_char

def honor(components):
   args = components['arguments'].split(CMD_STRING)
   if len(args) == 1:
      return USAGE_STRING
   phrase = args[1]
   if honor_functions.check_honor(phrase):
      response = phrase + " has honor."
   else:
      response = phrase + " is without honor."
   return response.encode('utf8')