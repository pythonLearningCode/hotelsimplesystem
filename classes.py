import sqlite3

#  CREATING THE DB IF IT NOT EXISTS
conn = sqlite3.connect("reservations.db")
cursor = conn.cursor()
create_table = 'CREATE TABLE IF NOT EXISTS reservation' \
'(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ' \
'name VARCHAR(200) NOT NULL, ' \
'date DATE, ' \
'registry VARCHAR(12),' \
'room INTEGER NOT NULL)'
cursor.execute(create_table)

#  cursor.execute('DELETE FROM reservation WHERE id > 4')
#  conn.commit()

#  CREATING THE CLIENTS CLASS WHERE ALL CLIENTS WILL BE INCLUDED IN THE DB

class Clients:
    def __init__(self, name, registry):
        self.name = name
        self.registry = registry

    def make_reservation(self, date, room):
        conn = sqlite3.connect("reservations.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reservation (name, date, registry, room) VALUES (?, ?, ?, ?)", (self.name, date, self.registry, room))
        conn.commit()
        cursor.close()
        conn.close()

'''
bob = Clients('bob', 202950978)
bob.make_reservation('2018-04-02', 2)
cursor.execute("SELECT * FROM reservation")
'''



#  CREATING THE FUNCTIONS THAT RETURNS A LIST OF THE NAMED COLUMN IN THE DB EACH

def show_ids():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    ids_list = []
    for line in cursor.fetchall():
        ids_list.append(line[0])
    cursor.close()
    conn.close()
    return ids_list

def show_names():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    names_list = []
    for line in cursor.fetchall():
        names_list.append(line[1])
    cursor.close()
    conn.close()
    return names_list


def show_resdates():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    dates_list = []
    for line in cursor.fetchall():
        dates_list.append(line[2])
    cursor.close()
    conn.close()
    return dates_list

def show_registrys():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    registrys_list = []
    for line in cursor.fetchall():
        registrys_list.append(line[3])
    cursor.close()
    conn.close()
    return registrys_list

def show_rooms():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    rooms_list = []
    for line in cursor.fetchall():
        rooms_list.append(line[4])
    cursor.close()
    conn.close()
    return rooms_list

#  DEFINING THE FUNCTION THAT REMOVES AN LINE ENTRY FROM THE DB
def rm_line(identifier):
    rm_id = identifier
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservation WHERE id = (?)", (rm_id))
    conn.commit()
    cursor.close()
    conn.close()



#  TESTING ....

if __name__ == '__main__':
    rm_line('1')
    show_ids()
    show_names()
    show_registrys()
    show_resdates()
    show_rooms()

cursor.close()
conn.close()






