# All Scripture quotations, unless otherwise indicated, are taken from The
# Holy Bible, English Standard Version. Copyright (c)2001 by Crossway Bibles
# (http://www.crosswaybibles.org), a publishing ministry of Good News
# Publishers. Used by permission. All rights reserved. Text provided by the
# Crossway Bibles Web Service (http://www.gnpcb.org/esv/share/services/).

from pythonbible import Passage
import os
import re
import requests
import scriptures

ESVAPI_KEY = ''
ESVAPI_URL = 'http://www.esvapi.org/v2/rest/passageQuery' 
ESVAPI_DEFAULT_PARAMS = {
	'output-format': 'plain-text',
	'include-passage-references': 'false',
	'include-headings': 'false',
	'include-subheadings': 'false',
	'include-heading-horizontal-lines': 'false',
	'include-passage-horizontal-lines': 'false',
	'include-footnotes': 'false',
	'include-short-copyright': 'false',
	'line-length': 1000000 # Arbitrarily high number
}

def MakeEsvApiRequest(data):
	LoadApiKeys()
	par = ESVAPI_DEFAULT_PARAMS
	par['key'] = ESVAPI_KEY
	par['passage'] = data
	return requests.get(ESVAPI_URL, params=par)

def LoadApiKeys():
	global ESVAPI_KEY
	if ESVAPI_KEY == '':
		api_key_file = open(os.path.join(os.getcwd(), '..', 'files', 'esvapi_key.dat'))
		ESVAPI_KEY = api_key_file.read()
		api_key_file.close()


def RemoveExtraWhitespace(text):
	text = text.replace('\r', '')
	text = text.replace('\n', '')
	text = text.replace(' ', '<>')
	text = text.replace('><', '')
	text = text.replace('<>', ' ')
	return text

def GetPassage(verse):
	'''
	Gets the text of the requested verse, in the requested language/translation.

	verse is a 5-value tuple:
	(Book name, start chapter, start verse, end chapter, end verse)
	'''
	passageSpec = '%(book)s+%(chap_start)s:%(v_start)s-%(chap_end)s:%(v_end)s' % {
		'book': verse[0],
		'chap_start': verse[1],
		'v_start': verse[2],
		'chap_end': verse[3],
		'v_end': verse[4]
	}
	resp = MakeEsvApiRequest(passageSpec)
	formatted_text = resp.text
	verses = ['[' + RemoveExtraWhitespace(v.strip()) for v in re.split(r'\[', formatted_text)[1:] if v.strip() != '']# First entry in verses is an empty string. Skip it.
	return '\r\n'.join(verses)

def bible(components):
	spec = components['arguments'].split('!bible ')[1]
	refs = scriptures.extract(spec)
	if len(refs) == 0:
		return ''
	response = ''
	verse_length = 0
	for r in refs:
		start_string = scriptures.reference_to_string(r[0], r[1], r[2], r[1], r[2])
		end_string = scriptures.reference_to_string(r[0], r[3], r[4], r[3], r[4])
		verse_length = verse_length + len(Passage(start_string, end_string))
		if verse_length > 5:
			return 'Could not fetch verses: length of passage too long'.encode('utf8')
		vs = GetPassage(r)
		response = '%(old_resp)s%(spec)s (ESV)\r\n%(verses)s\r\n' % {
			'old_resp': response,
			'spec': scriptures.reference_to_string(r[0], r[1], r[2], r[3], r[4]),
			'verses': vs
		}
	return response.encode('utf8')

if __name__ == "__main__":
	comp = {}
	comp['arguments'] = '!bible Philemon 1'
	print bible(comp)
