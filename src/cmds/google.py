from apiclient.discovery import build
from config import cmd_char

CMD_STRING = cmd_char + 'google ' # Note the trailing space!
USAGE_STRING = 'Usage: %sgoogle <search term>' % cmd_char

def google(components): # !google <search term>
   '''Returns the link and the description of the first result from a google search'''
   response = ''

   terms = components['arguments'].split(CMD_STRING)

   if 2 == len(terms) and 1 <= len(terms[1].lstrip()):
      service = build("customsearch", "v1", developerKey="AIzaSyCy6tveUHlfNQDUtH0TJrF6PtU0h894S2I")

      res = service.cse().list(
         q = terms[1].lstrip(),
         cx = '005983647730461686104:qfayqkczxfg',
      ).execute()

      if 1 <= res['queries']['request'][0]['totalResults']:
         result = res['items'][0]
         response = result['link'] + '\r\n' + result['snippet']

      else:
         response = 'Not found: ' + terms[1]

   else:
      response = USAGE_STRING

   return str(response.encode('utf8'))
