import bible_functions
from pythonbible import Passage
import re
import scriptures

PASSAGE_PATTERN = re.compile(r"\[(.*?)\]", re.IGNORECASE)

def auto_bible(components):
   matches = PASSAGE_PATTERN.findall(components['arguments'])
   refs = []
   for m in matches:
      new_ref = scriptures.extract(m)
      if len(new_ref) == 1:
         refs.append(new_ref[0])

   if len(refs) == 0:
      return

   response = ''
   verse_length = 0
   for r in refs:
      start_string = scriptures.reference_to_string(r[0], r[1], r[2], r[1], r[2])
      end_string = scriptures.reference_to_string(r[0], r[3], r[4], r[3], r[4])
      verse_length = verse_length + len(Passage(start_string, end_string))
      if verse_length > 5:
         return 'Could not fetch verses: length of passage too long'.encode('utf8')
      vs = bible_functions.GetPassage2(r)
      response = '%(old_resp)s%(spec)s (ESV)\r\n%(verses)s\r\n' % {
         'old_resp': response,
         'spec': scriptures.reference_to_string(r[0], r[1], r[2], r[3], r[4]),
         'verses': vs
      }
   return response.encode('utf-8')

if __name__ == '__main__':
   comp = {}
   comp['arguments'] = "[Not a bible ref] [John 3:16]"
   print auto_bible(comp).encode('utf-8')