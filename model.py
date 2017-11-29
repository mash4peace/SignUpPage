import sqlite3 as sql
def insertUser(firstname, lastname, email, password):
    cnn = sql.connect('hasm.db')
    cur = cnn.cursor()
    cur.execute('''INSERT INTO Register(firstname, lastname, email, password) VALUES(?,?,?,?)''', (firstname, lastname, email, password))
    cnn.commit()
    cnn.close()
def userEixts(email):
    email = email
    cnn = sql.connect('hasm.db')
    cur = cnn.cursor()
    cur.execute('''SELECT email from Register WHERE email = ?''', (email,))
    data = cur.fetchall()
    if len(data) == 0:
        print('User with e-mail ' + email + " not found!")
        cnn.close()
        return False
    else:
        print("User with email " + email+ " found")
        cnn.close()
        return True


def getPassword(email):
    email = email
    cnn = sql.connect('hasm.db')
    cur = cnn.cursor()
    cur.execute('''SELECT password FROM Register WHERE email = ?''', (email,))
    data = cur.fetchall()
    d = data[0]
    cnn.close()
    return d[0]
