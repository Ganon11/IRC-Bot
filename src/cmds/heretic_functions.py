import os
import re
import sqlite3

heretic_pattern = re.compile(r"(\w+) is a heretic", re.IGNORECASE)
non_heretic_pattern = re.compile(r"(\w+) is not a heretic", re.IGNORECASE)

def build_heretics_db():
	conn = sqlite3.connect(os.path.join(os.getcwd(), '..', '..', 'files', 'heretics.db'))
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS Heretics (name text PRIMARY KEY, count integer)""")
	conn.commit()
	conn.close()

def add_heretic(target):
	conn = sqlite3.connect(os.path.join(os.getcwd(), '..', '..', 'files', 'heretics.db'))
	cur = conn.cursor()
	data = (target,)
	cur.execute("""SELECT * FROM Heretics WHERE name=?""", data)
	result = cur.fetchone()
	if result is None:
		cur.execute("""INSERT INTO Heretics VALUES (?,1)""", data)
	else:
		data = (result[1] + 1, target)
		cur.execute("""UPDATE Heretics SET count=? WHERE name=?""", data)

	conn.commit()
	conn.close()

def remove_heretic(target):
	conn = sqlite3.connect(os.path.join(os.getcwd(), '..', '..', 'files', 'heretics.db'))
	cur = conn.cursor()
	data = (target,)
	cur.execute("""SELECT * FROM Heretics WHERE name=?""", data)
	result = cur.fetchone()
	if result is None:
		pass
	else:
		data = (result[1] - 1, target)
		cur.execute("""UPDATE Heretics SET count=? WHERE name=?""", data)

	conn.commit()
	conn.close()

def get_heretics(count=5):
	responses = ['Top heretics of #reddit-Christianity']
	conn = sqlite3.connect(os.path.join(os.getcwd(), '..', '..', 'files', 'heretics.db'))
	cur = conn.cursor()
	cur.execute("""SELECT * FROM Heretics ORDER BY count DESC""")
	results = cur.fetchall()
	for i in range(count - 1):
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