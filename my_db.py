import sqlite3

class Data_base:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS student
        (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT,code_meli TEXT, score REAL)''')
        self.con.commit()

    def insert(self,fname,lname,code_meli,score):
        self.cur.execute('INSERT INTO student VALUES (NULL,?,?,?,?)',(fname, lname, code_meli, score))
        self.con.commit()

    def select(self):
        self.cur.execute('SELECT * FROM student')
        return self.cur.fetchall()
        
    def delete(self,id):
        self.cur.execute('DELETE from student WHERE id = ?',(id,))
        self.con.commit()
    
    def update(self,id,fname,lname,code_meli,score):
        self.cur.execute('UPDATE student SET fname = ?,lname = ?,code_meli = ? ,score = ? WHERE id = ? '
                         ,(fname,lname,code_meli,score,id))
        self.con.commit()