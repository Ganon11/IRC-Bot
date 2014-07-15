# All Scripture quotations, unless otherwise indicated, are taken from The
# Holy Bible, English Standard Version. Copyright (c)2001 by Crossway Bibles
# (http://www.crosswaybibles.org), a publishing ministry of Good News
# Publishers. Used by permission. All rights reserved. Text provided by the
# Crossway Bibles Web Service (http://www.gnpcb.org/esv/share/services/).

from bs4 import BeautifulSoup
from pythonbible import Passage
import json
import os
import re
import requests
import scriptures
import sys

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
   LoadApiKey()
   par = ESVAPI_DEFAULT_PARAMS
   par['key'] = ESVAPI_KEY
   par['passage'] = data
   return requests.get(ESVAPI_URL, params=par)

def LoadApiKey():
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
   text = re.sub(r'<h\d(?: \w+="[\w\d\.]+")+>.+?</h\d>', '', text)
   text = re.sub(r'<p(?: \w+="[\w\d\.]+")+>', '', text)
   text = re.sub(r'</p>', '', text)
   text = re.sub(r'<span(?: \w+="[\w\d\.]+")+>(.+?)</span>', r'\1', text)
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

################################################################################
# Attempt to get bibles.org working. Thanks to _joe from IRC for some of the
# initial work!
################################################################################

BIBLES_KEY = ''
BIBLES_URL = 'https://bibles.org/v2/passages.js'
BIBLES_DEFAULT_PARAMS = {
   'version': 'eng-ESV'
}

def MakeBiblesRequest(data, version=None):
   LoadBiblesKey()
   par = BIBLES_DEFAULT_PARAMS
   par['q[]'] = data
   if version is not None:
      if re.search(r'^[a-z]+-', version) is None:
         version = 'eng-' + version
      par['version'] = version
   return requests.get(BIBLES_URL, params=par, auth=requests.auth.HTTPBasicAuth(BIBLES_KEY, 'X'))

def LoadBiblesKey():
   global BIBLES_KEY
   if BIBLES_KEY == '':
      api_key_file = open(os.path.join(os.getcwd(), '..', 'files', 'bibles_org_api_key.dat'))
      BIBLES_KEY = api_key_file.read()
      api_key_file.close()

def GetPassage2(verse):
   passageSpec = scriptures.reference_to_string(verse[0], verse[1], verse[2], verse[3], verse[4])
   passages = json.loads(MakeBiblesRequest(passageSpec, verse[5]).text)['response']['search']['result']['passages']
   verses = []
   if len(passages) > 0:
      text = RemoveExtraWhitespace(passages[0]['text'])
      verses = re.split(r'<sup(?: \w+="[\w\d\.-]+")+>[\d-]+</sup>', text)
      verses = [ x for x in verses if x != '' ]

   return '\r\n'.join(verses).encode('utf-8')

if __name__ == "__main__":
   text = '1 Maccabees 1:1 KJVA'
   verse = scriptures.extract(text)
   print verse
   result = GetPassage2(verse[0])
   print result
