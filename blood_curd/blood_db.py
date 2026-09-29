import mysql.connector
class DonorListCreateRetriveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="blood_db")
        print(self.con)
        self.cursor=self.con.cursor()
        print("successfully connected")

    def List(self):
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            return records
        else:
            print("no records found")

    def Create(self,id,name,blood_group,city,phone,last_donation):
        query="insert into donor(id,name,blood_group,city,phone,last_donation)values(%s,%s,%s,%s,%s,%s)";
        data=(id,name,blood_group,city,phone,last_donation)
        self.cursor.execute(query,data)
        self.con.commit()
        print("insert data successfully")

    def Retrive(self, id):
        query = "select * from donor where id=%s"
        data = (id,)
        self.cursor.execute(query, data)

        records = self.cursor.fetchone()
        if records:
            return (records)
        else:
            print("no records found")

    def Update(self,id,name,blood_group,city,phone,last_donation ):
        query = "update donor set name=%s,blood_group=%s,city=%s,phone=%s,last_donation=%s where id=%s"
        data = (name,blood_group,city,phone,last_donation ,id)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def Delete(self, id):
        query = "DELETE FROM donor WHERE id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            return (True)
        else:
            return (False)

do =DonorListCreateRetriveUpdateDelete()