# All Scripture quotations, unless otherwise indicated, are taken from The
# Holy Bible, English Standard Version. Copyright (c)2001 by Crossway Bibles
# (http://www.crosswaybibles.org), a publishing ministry of Good News
# Publishers. Used by permission. All rights reserved. Text provided by the
# Crossway Bibles Web Service (http://www.gnpcb.org/esv/share/services/).

from config import cmd_char
import bible_functions
from pythonbible import Passage
import scriptures
import sys

CMD_STRING = cmd_char + 'bible '
USAGE_STRING = 'Usage: %sbible <passage specifier>' % cmd_char

def bible(components):
   args = components['arguments'].split(CMD_STRING)
   if len(args) == 1:
      return USAGE_STRING
   spec = args[1]
   refs = scriptures.extract(spec)
   if len(refs) == 0:
      return USAGE_STRING
   response = ''
   verse_length = 0
   for r in refs:
      start_string = scriptures.reference_to_string(r[0], r[1], r[2], r[1], r[2])
      end_string = scriptures.reference_to_string(r[0], r[3], r[4], r[3], r[4])
      verse_length = verse_length + len(Passage(start_string, end_string))
      if verse_length > 5:
         return 'Could not fetch verses: length of passage too long'.encode('utf8')
      vs = bible_functions.GetPassage(r)
      response = '%(old_resp)s%(spec)s (ESV)\r\n%(verses)s\r\n' % {
         'old_resp': response,
         'spec': scriptures.reference_to_string(r[0], r[1], r[2], r[3], r[4]),
         'verses': vs
      }
   return response.encode('utf8')

if __name__ == "__main__":
   comp = {}
   if len(sys.argv) > 1:
      comp['arguments'] = '!bible %s' % ' '.join(sys.argv[1:])
   else:
      comp['arguments'] = '!bible John 3:16'
   print bible(comp)
