import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    found = re.search("^From \S*@(\S*)",line)
    if found:
        institute=found.group(1)
        print (institute)
    else:
        continue
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (institute,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (institute,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (institute,))
    conn.commit()

#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'


cur.close()
