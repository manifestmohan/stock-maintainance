import sqlite3

def connect():
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS lps_table(id INTEGER PRIMARY KEY,Item_Name text,Price_code text,Quantity integer,Dealer_name text)")
    conn.commit()
    conn.close()

def insert(Item_Name,Price_code,Quantity,Dealer_name):
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO lps_table VALUES (NULL,?,?,?,?)",(Item_Name,Price_code,Quantity,Dealer_name))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM lps_table")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(Item_Name="",Price_code="",Quantity="",Dealer_name=""):
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM lps_table WHERE Item_Name = ? OR Price_code = ? OR Quantity = ? OR Dealer_name = ?",(Item_Name,Price_code,Quantity,Dealer_name))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM lps_table WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,Item_Name,Price_code,Quantity,Dealer_name):
    conn = sqlite3.connect("lps.db")
    cur = conn.cursor()
    cur.execute("UPDATE lps_table SET Item_Name=?, Price_code=?, Quantity=?, Dealer_name=? WHERE id=?",(Item_Name,Price_code,Quantity,Dealer_name,id))
    conn.commit()
    conn.close()

connect()
update(2,'flower','ade',20,'bbbbb')
print(view())
