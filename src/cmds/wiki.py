#!python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from config import cmd_char
import urllib2

CMD_STRING = cmd_char + 'wiki ' # Note the trailing space!

def wiki(components): # !wiki <search term>
   '''Returns a wiki link and the first paragraph of the page'''

   main_page = 'http://en.wikipedia.org/wiki/Main_Page'

   wlink = components['arguments'].split(CMD_STRING) # notice the trailing space
   if 1 == len(wlink): # no search term given, the Main_Page is "displayed"
      response = main_page
   else:
      search_term = wlink[1].lstrip().replace(' ', '_')

      if len(search_term) < 1:
         response = main_page
      else:
         response = 'http://en.wikipedia.org/wiki/' + search_term

   response = response + '\r\n' + get_paragraph(response)

   return response

def get_paragraph(wlink):
   '''Gets the first paragraph from a wiki link'''

   msg = ''
   try:
      page_request = urllib2.Request(wlink)
      page_request.add_header('User-agent', 'Mozilla/5.0')
      page = urllib2.urlopen(page_request)
   except IOError:
      msg = 'Cannot access link!'
   else:

      soup = BeautifulSoup(page)
      msg = ''
      try:
         msg = ''.join(soup.find('div', { 'id' : 'bodyContent'}).p.findAll(text=True))
      except AttributeError:
         return 'Wikipedia does not have an encyclopedic article for your search term.'

      while 460 < len(msg): # the paragraph cannot be longer than 510
         # characters including the protocol command
         pos = msg.rfind('.')
         msg = msg[:pos]

   return msg.encode('utf-8')

if __name__ == "__main__":
   comp = {}
   comp['arguments'] = '!wiki Einheitsübersetzung'
   print wiki(comp)
