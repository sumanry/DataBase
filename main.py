import sqlite3

con = sqlite3.connect('mycompany.db')
cObj = con.cursor()

cObj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
con.commit()

def insert_value(id, name, salary, department, position):
    cObj.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(id, name, salary, department,position))
    con.commit()

def Update_department(dep, id):
    cObj.execute("UPDATE employees SET department = ? WHERE id = ?",(dep, id))
    con.commit()

def sql_fetch():
    cObj.execute("SELECT * FROM employees")
    result = cObj.fetchall()
    print(result)

def delete_all():
    cObj.execute("DELETE FROM employees")
    con.commit()

insert_value(1, "Shubham", 80000, "Python", "Developer")
#delete_all()

cObj.close()
con.close()