
import mysql.connector
class BookListCreateRetriveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="libary")

        print(self.con)

        self.cursor=self.con.cursor()
        print("successfully connected")
    #
    def List(self):
            query = "SELECT * FROM book"
            self.cursor.execute(query)

            records = self.cursor.fetchall()
            if records:

                return records

            else:
                print("no records found")
    def Create(self,id,title,author,price,language,pages):
        query="insert into book(id,title,author,price,language,pages)values(%s,%s,%s,%s,%s,%s)";
        data=(id,title,author,price,language,pages)
        self.cursor.execute(query,data)
        self.con.commit()
        print("insert data successfully")
    def Retrive(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)

        records = self.cursor.fetchone()
        if records:
                return(records)
        else:
              print("no records found")

    def Update(self,title,author,price,language,pages,id):
        query="update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id=%s"
        data = (title, author, price, language, pages,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False
    def Delete(self, id):
        query = "DELETE FROM book WHERE id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            return (True)
        else:
            return (False)

book_instance=BookListCreateRetriveUpdateDelete()
# book_instance.List()
# book_instance.Create('102','abc','jons','9000','english','10000')
# book_instance.Retrive(102)
# book_instance.Delete(102)
# book_instance.Update('abc','rani','90','malayalam','600','106')