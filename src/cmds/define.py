from bs4 import BeautifulSoup
from config import cmd_char
import os
import requests

CMD_STRING = cmd_char + 'define ' # note the trailing space!
DICTIONARYAPI_URL = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
DICTIONARYAPI_KEY = ''
USAGE_STRING = 'Usage: %sdefine <term>' % cmd_char

def MakeDictionaryApiRequest(data):
	LoadApiKey()
	par = {}
	par['key'] = DICTIONARYAPI_KEY
	return requests.get(DICTIONARYAPI_URL + data, params=par)

def LoadApiKey():
	global DICTIONARYAPI_KEY
	if DICTIONARYAPI_KEY == '':
		api_key_file = open(os.path.join(os.getcwd(), '..', '..', 'files', 'dictionaryapi_key.dat'))
		DICTIONARYAPI_KEY = api_key_file.read()
		api_key_file.close()

def define(components):
	args = components['arguments'].split(CMD_STRING)
	if len(args) == 1:
		return USAGE_STRING
    phrase = args[1]
    soup = BeautifulSoup(MakeDictionaryApiRequest(phrase).text)
    response = []
    #print soup.entry_list.entry
    string = '%(word)s (%(pronunciation)s)' % { 'word' : phrase, 'pronunciation' : soup.entry_list.entry.pr.text.encode('utf8')}
    print string
    response.append(string)
    print response
    return ('\r\n'.join(response)).encode('utf8')

if __name__ == '__main__':
	comp = {}
	comp['arguments'] = '!define hypocrite'
	print define(comp)