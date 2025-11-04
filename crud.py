import sqlite3
conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT)")

cur.execute("INSERT INTO contacts (nom, prenom) VALUES (?, ?)", ("FLou", "Claire"))

for row in cur.execute('SELECT * FROM contacts'):
    print(row)

cur.execute("UPDATE contacts SET prenom = ? WHERE id = ?", ("Claire", "1"))

cur.execute("DELETE FROM contacts WHERE id = ?", (1,))

conn.commit()
conn.close()

def _insert_row(self, nom, prenom):
    cursor = self.conn.cursor()
    cursor.execute("INSERT INTO contacts(nom, prenom) VALUES (?, ?)", (nom, prenom))
    self.conn.commit()

def _fetch_all(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT nom, prenom FROM contacts ORDER BY id DESC")
    return cur.fetchall()

def _update(self, nom, prenom):
    self.conn.execute("UPDATE contacts SET nom = ?, prenom = ? WHERE id = ?", (nom, prenom, 1) )

    self.conn.commit()

def _delete(self, nom, prenom):
    self.conn.execute("DELETE FROM contacts WHERE nom = ?", (nom, ) )
    self.conn.commit()