import mysql.connector
class VehicleListCreateRetriveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="shabna",host="localhost",database="vehicle")

        print(self.con)

        self.cursor=self.con.cursor()
        print("successfully connected")



    # def List(self):
    #         query = "SELECT * FROM vehicle"
    #         self.cursor.execute(query)
    #
    #         records = self.cursor.fetchall()
    #         if records:
    #             for row in records:
    #                 print(row)
    #         else:
    #             print("no records found")


    # def Create(self,vehicle_id,vehicle_name,brand,price,model):
    #     query="insert into vehicle(vehicle_id,vehicle_name,brand,price,model)values(%s,%s,%s,%s,%s)"
    #     data=(vehicle_id,vehicle_name,brand,price,model)
    #     self.cursor.execute(query,data)
    #     self.con.commit()
    #     print("insert data successfully")



    # def Retrive(self,vehicle_id):
    #     query="select * from vehicle where vehicle_id=%s"
    #     data=(vehicle_id,)
    #     self.cursor.execute(query,data)
    #     records=self.cursor.fetchall()
    #     if records:
    #         for row in records:
    #             print(row)
    #     else:
    #         print("no record found")

    # def Delete(self,vehicle_id):
    #     query="Delete from vehicle where vehicle_id=%s"
    #     data=(vehicle_id,)
    #     self.cursor.execute(query, data)
    #     self.con.commit()
    #
    #     if self.cursor.rowcount > 0:
    #         print("vehicle deleted successfully")
    #     else:
    #         print("vehicle not found")
    def Update(self, vehicle_id, vehicle_name, brand, price, model):
        query = "UPDATE vehicle SET vehicle_name=%s, brand=%s, price=%s, model=%s WHERE vehicle_id=%s"

        data = (vehicle_name, brand, price, model, vehicle_id)

        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            print("Vehicle updated successfully")
        else:
            print("Vehicle not found")

v=VehicleListCreateRetriveUpdateDelete()
# v.List()
# v.Create(1, "Swift", "Maruti", 800000, "abs")
# v.Retrive(1)
# v.Delete(1)
v.Update(1, "swift", "maruti", 800000, "absc")