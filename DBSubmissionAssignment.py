import sqlite3


conn = sqlite3.connect('D_Bsa.db')

# creating the table for database poodles

with conn:
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS tbl_poodles (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT)")
    conn.commit()
conn.close()

def addTXT(fileList):
    conn = sqlite3.connect('D_Bsa.db')

# adding info into the table

    with conn:
        cur = conn.cursor()
        for i in fileList:
            if i.endswith(".txt"):
                print(i)
                cur.execute ("INSERT INTO tbl_poodles (col_name) VALUES (?)",(i,))
        conn.commit()
    conn.close()

if __name__ == "__main__":
       
    fileList = ('information.docx','Hello.txt','myImage.png',\
                'myMovie.mpg','World.txt','data.pdf','myPhoto.png','graffititxt.png')

    addTXT(fileList)
