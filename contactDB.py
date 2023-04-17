
import mariadb


class contactDB:
    '''
    A class for interfacing with a contacts mysql database
    '''

    def __init__(self):
        '''
        Create a connection to the database
        '''
        HOST = "localhost"
        USER = "Fiifi"
        DB = "contactDir"
        PASS = "yawson123"

        self.mydb = mariadb.connect(
            host=HOST,
            user=USER,
            passwd=PASS,
            database=DB
        )
        return

    def find(self, search):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM contact WHERE Last like '%"+search +
                         "%' OR First like '%"+search+"%' OR Type like '%"+search+"%'")
        myresult = mycursor.fetchall()
        return(myresult)

    def findByLast(self, last):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM contact WHERE Last like '%"+last+"%'")
        myresult = mycursor.fetchall()
        return(myresult)

    def findByFirst(self, first):
        mycursor = self.mydb.cursor()
        mycursor.execute(
            "SELECT * FROM contact WHERE First like '%"+first+"%'")
        myresult = mycursor.fetchall()
        return(myresult)

    def delete(self, idnum):
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute("DELETE FROM contact WHERE ID='"+idnum+"'")
            self.mydb.commit()
        except Exception as e:
            return '{"status","Error","reason":"' + str(e) + '"}'
        return '{"status":"success"}'

    def add(self, first, last, phone, ptype):
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute("INSERT INTO contact(First,Last,Phone,Type) VALUES ('" +
                             first+"','"+last+"','"+phone+"','"+ptype+"')")
            self.mydb.commit()
        except Exception as e:
            return '{"status":"Error","reason":"' + str(e) + '"}'

        return '{"status":"success"}'

    def update(self, idnum, first, last, phone, ptype):
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute("UPDATE contact SET First = '"+first+"', Last ='" +
                             last+"', Phone ='"+phone+"', Type ='"+ptype+"' WHERE ID='"+idnum+"'")
            self.mydb.commit()
        except Exception as e:
            return '{"status","Error","reason":"' + str(e) + '"}'
        return '{"status":"success"}'
