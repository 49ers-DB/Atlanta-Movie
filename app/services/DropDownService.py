import DBService

class DropDownService(object):


    def CompanyDropDown(self):

        connection = DBService.get_conn()
        with connection.cursor() as cursor:
    #Manager-Only Registration, Manager-Customer Registration, Manage Company, Create Theater
    # Explore Movie, Explore Theater, Visit History
            
            sql = """SELECT comName FROM Company"""
            cursor.execute(sql)
            data=cursor.fetchall()
            connection.commit()
            connection.close()
            return data


    def ManagerDropDown(self):

        connection = DBService.get_conn()

        with connection.cursor() as cursor:
    #Create Theater

            query = "select firstname, lastname from User inner join Manager on Manager.username = User.username"
        
            connection.close()


    def MovieDropDown(self):

        connection = DBService.get_conn()

        with connection.cursor() as cursor:
    #Schedule Movie, Explore Movie

            query = "select movName from Movie"

            connection.close()


    def TheaterDropDown(self, companyName):

        connection = DBService.get_conn()

        with connection.cursor() as cursor:

            query = """select thName from Theater
                    where comName=(%s)"""
            cursor.execute(query, (companyName))
            data=cursor.fetchall()
            connection.commit()

            connection.close()
            
            return data







