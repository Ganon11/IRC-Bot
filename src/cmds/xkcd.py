from config import cmd_char
import HTMLParser
import json
import os
import sqlite3
import urllib

CMD_STRING = cmd_char + 'xkcd ' # Note the trailing space!
USAGE_STRING = 'Usage: %sxkcd <[number] OR [search term]>' % cmd_char

def xkcd(components):
   ''' Returns xkcd comic data given a user's search (comic number/name or search term)
   '''
   build_comics_db()  # first time this is run could take awhile...
   response = ''
   args = components['arguments'].split(CMD_STRING)
   if len(args) == 1:
      return USAGE_STRING
   search = args[1].lstrip()

   if search.isdigit():
      response = get_comic(search)
   else:
      data = search_comics(search)
      if data != None:
         response = data[0] + " - http://xkcd.com/" + str(data[2]) + "\r\n" + data[1]
      else:
         response = "No comic found!"
   return response.encode('utf8')


def get_comic(comic_num):
   ''' Gets the link and alt - text to the comic specified
   by the input integer
   '''
   try:
      response = urllib.urlopen("http://xkcd.com/{}/info.0.json".format(comic_num))
   except:
      return "Comic doesn't exist!"
   data = json.load(response)
   return data["title"] + " - http://xkcd.com/{}".format(comic_num) + "\r\n" + data["alt"]


def get_latest_comic():
   ''' Gets the latest comic
   '''

   try:
      response = urllib.urlopen("http://xkcd.com/info.0.json")
      data = json.load(response)
   except:
      return "Error getting latest comic!"
   return data


def build_comics_db():
   ''' Builds the database and appends new comics when found
   '''
   conn = sqlite3.connect(os.path.join(os.getcwd(), '..', 'files', 'comics.db'))
   cur = conn.cursor()
   h = HTMLParser.HTMLParser()

   cur.execute("""CREATE TABLE IF NOT EXISTS Comics (title text, alt text, comic_num integer PRIMARY KEY)""")
   last_comic = cur.execute("SELECT MAX(comic_num) FROM Comics LIMIT 1")
   last_comic = last_comic.fetchone()[0]
   if last_comic == None:
      last_comic = 0

   latest = get_latest_comic()
   for i in range(last_comic + 1, latest["num"] + 1):
      if i == 404:
         data = {
            'title': '404',
            'alt': '404 - Not Found',
            'num': 404
         }
      else:
         try:
            response = urllib.urlopen("http://xkcd.com/{}/info.0.json".format(i))
         except:
            return "Error getting latest comic!"
         data = json.load(response)
      cur.execute("""INSERT INTO Comics (title, alt, comic_num) VALUES (?,?,?)""", (h.unescape(data["title"]), h.unescape(data["alt"]), data["num"]))
   cur.close()
   conn.commit()
   conn.close()
   return


def search_comics(search):
   ''' Searchs the database for comics with specified name.
   Failing that, it looks for comics that contain the search term
   in alt - text
   '''
   conn = sqlite3.connect(os.path.join(os.getcwd(), '..', 'files', 'comics.db'))
   cur = conn.cursor()
   query = "SELECT * FROM Comics WHERE title = ? COLLATE NOCASE"
   response = cur.execute(query, (search,))
   data = response.fetchone()
   if data != None:
      return data

   query = "SELECT * FROM Comics WHERE alt LIKE ?"
   search = '%' + search + '%'
   r = cur.execute(query, (search,))
   data = r.fetchone()
   if data != None:
      return data
   cur.close()
   conn.close()
   return None
