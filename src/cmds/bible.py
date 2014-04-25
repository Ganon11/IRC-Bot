import json
import os
import requests
import scriptures

BIBLES_ORG_API_KEY = ''
BIBLES_ORG_API_PASS = 'X'
BIBLES_ORG_API_VER = 'v2'
BIBLES_ORG_CHAPTERS = 'chapters'
BIBLES_ORG_URL = 'https://bibles.org'
BIBLES_ORG_VERSES = 'verses'
BIBLES_ORG_VERSIONS = 'versions'
DEFAULT_LANGUAGE = 'eng'
DEFAULT_VERSION = 'KJVA'

BOOKS_TO_BOOKS = {
	# Old Testament
	'Genesis': 'Gen',
	'Exodus' : 'Exod',
	'Leviticus' : 'Lev',
	'Numbers' : 'Num',
	'Deuteronomy' : 'Deut',
	'Joshua' : 'Josh',
	'Judges' : 'Judg',
	'Ruth' : 'Ruth',
	'I Samuel' : '1Sam',
	'II Samuel' : '2Sam',
	'I Kings' : '1Kgs',
	'II Kings' : '2Kgs',
	'I Chronicles' : '1Chr',
	'II Chronicles' : '2Chr',
	'Ezra' : 'Ezra',
	'Nehemiah' : 'Neh',
	'Esther' : 'Esth',
	'Job' : 'Job',
	'Psalms' : 'Ps',
	'Proverbs' : 'Prov',
	'Ecclesiastes' : 'Eccl',
	'Song of Solomon' : 'Song',
	'Isaiah' : 'Isa',
	'Jeremiah' : 'Jer',
	'Lamentations' : 'Lam',
	'Ezekiel' : 'Ezek',
	'Daniel' : 'Dan',
	'Hosea' : 'Hos',
	'Joel' : 'Joel',
	'Amos' : 'Amos',
	'Obadiah' : 'Obad',
	'Jonah' : 'Jonah',
	'Micah' : 'Mic',
	'Nahum' : 'Nah',
	'Habakkuk' : 'Hab',
	'Zephaniah' : 'Zeph',
	'Haggai' : 'Hag',
	'Zechariah' : 'Zech',
	'Malachi' : 'Mal',

	#Deuterocanon
	'Tobit' : 'Tob',
	'Judith' : 'Jdt',
	'Esther (Greek)' : 'AddEsth',
	'The Wisdom of Solomon' : 'Wis',
	'Sirach' : 'Sir',
	'Baruch' : 'Bar',
	'Letter of Jeremiah' : 'EpJer',
	'1 Maccabees' : '1Macc',
	'2 Maccabees' : '2Macc',
	'1 Esdras' : '1Esd',
	'2 Esdras' : '2Esd',
	'The Prayer of Manasseh' : 'PrMan',

	#New Testament
	'Matthew' : 'Matt',
	'Mark' : 'Mark',
	'Luke' : 'Luke',
	'John' : 'John',
	'Acts' : 'Acts',
	'Romans' : 'Rom',
	'I Corinthians' : '1Cor',
	'II Corinthians' : '2Cor',
	'Galatians' : 'Gal',
	'Ephesians' : 'Eph',
	'Philippians' : 'Phil',
	'Colossians' : 'Col',
	'I Thessalonians' : '1Thess',
	'II Thessalonians' : '2Thess',
	'I Timothy' : '1Tim',
	'II Timothy' : '2Tim',
	'Titus' : 'Titus',
	'Philemon' : 'Phlm',
	'Hebrews' : 'Heb',
	'James' : 'Jas',
	'I Peter' : '1Pet',
	'II Peter' : '2Pet',
	'I John' : '1John',
	'II John' : '2John',
	'III John' : '3John',
	'Jude' : 'Jude',
	'Revelation of Jesus Christ' : 'Rev'
}

def MakeRequest(url):
	r = requests.get(url, auth=(BIBLES_ORG_API_KEY, BIBLES_ORG_API_PASS))
	return r

def LoadApiKey():
	global BIBLES_ORG_API_KEY
	if BIBLES_ORG_API_KEY == '':
		api_key_file = open(os.path.join(os.getcwd(), '..', '..', 'files', 'bibles_org_api_key.dat'))
		BIBLES_ORG_API_KEY = api_key_file.read()

def GetVerse(verse, lang=DEFAULT_LANGUAGE, version=DEFAULT_VERSION):
	'''
	Gets the text of the requested verse(s), in the requested language/translation.

	verse is a 5-value tuple:
	(Book name, start chapter, start verse, end chapter, end verse)
	'''
	LoadApiKey()
	request_url = '%(url_base)s/%(api_ver)s/%(action)s/%(language)s-%(translation)s:%(book)s.%(chapter)s.%(verse)s.js' % {
		'url_base': BIBLES_ORG_URL,
		'api_ver': BIBLES_ORG_API_VER,
		'action': BIBLES_ORG_VERSES,
		'language': lang,
		'translation': version,
		'book': BOOKS_TO_BOOKS[verse[0]],
		'chapter': verse[1],
		'verse': verse[2]
	}
	print 'Making request to ' + str(request_url)
	resp = MakeRequest(request_url)
	print 'Got response ' + str(resp.text)

if __name__ == '__main__':
	myVerse = ('Romans', 1, 1, 1, 10)
	GetVerse(myVerse)