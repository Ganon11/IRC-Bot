import os
import re
import sqlite3

singular_heretic_pattern = re.compile(r"(\w+) is a heretic", re.IGNORECASE)
plural_heretic_pattern = re.compile(r"(\w+) are heretics", re.IGNORECASE)
singular_non_heretic_pattern = re.compile(r"(\w+) is not a heretic", re.IGNORECASE)
plural_non_heretic_pattern = re.compile(r"(\w+) are not heretics", re.IGNORECASE)
db_file_path = os.path.join(os.getcwd(), '..', 'files', 'heretics.db')

def build_heretics_db():
	conn = sqlite3.connect(db_file_path)
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS Heretics (username text, heretic text, vote integer, CONSTRAINT PK_Heretics PRIMARY KEY (username, heretic))""")
	conn.commit()
	conn.close()

def change_heretic(user, target, vote):
	conn = sqlite3.connect(db_file_path)
	cur = conn.cursor()
	data = (user, target)
	cur.execute("""SELECT * FROM Heretics WHERE username=? AND heretic=?""", data)
	result = cur.fetchone()
	if result is None:
		data = (user, target, vote)
		cur.execute("""INSERT INTO Heretics VALUES (?,?,?)""", data)
	else:
		data = (vote, user, target)
		cur.execute("""UPDATE Heretics SET vote=? WHERE username=? AND heretic=?""", data)

	conn.commit()
	conn.close()

def get_heretic(target):
	conn = sqlite3.connect(db_file_path)
	cur = conn.cursor()
	data = (target.lower(),)
	cur.execute("""SELECT SUM(vote) AS score FROM Heretics AS h WHERE LOWER(h.heretic) LIKE LOWER(?)""", data)
	result = cur.fetchone()
	count = 0
	try:
		count = int(result[0])
	except:
		pass
	conn.close()
	return count

def get_heretics(count=5):
	if count > 10:
		count = 10
	responses = ['Top Heretics']
	conn = sqlite3.connect(db_file_path)
	cur = conn.cursor()
	cur.execute("""SELECT heretic, SUM(vote) AS score FROM Heretics GROUP BY heretic ORDER BY score DESC""")
	results = cur.fetchall()
	for i in range(count):
		if (i < len(results)):
			responses.append('   #%(num)s %(name)s (%(count)s denunciations)' % {
				'num': i + 1,
				'name': results[i][0],
				'count': results[i][1]
			})
		else:
			break

	conn.close()
	return '\r\n'.join(responses)

if __name__ == '__main__':
	build_heretics_db()
	change_heretic('mstark', 'Arius', 1)
	print get_heretics()
	change_heretic('sprherowithnopwr', 'Arius', 1)
	print get_heretics()
	change_heretic('mstark', 'Arius', 1)
	print get_heretics()