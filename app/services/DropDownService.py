from app.services.DBService import get_conn

class DropDownService(object):


    def CompanyDropDown(self):

        connection = get_conn()
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

        connection = get_conn()

        with connection.cursor() as cursor:

            query = """select firstname, lastname, Manager.username from User
                inner join Manager on Manager.username = User.username
                where Manager.username not in
                (select manUsername from Theater)"""

            cursor.execute(query)
            managers = cursor.fetchall()
        
        connection.close()
        return {'ok':True, 'managers':managers}


    def MovieDropDown(self):

        connection = get_conn()
        data = {}

        with connection.cursor() as cursor:

            query = "select movName, movReleaseDate from Movie"
            cursor.execute(query)
            data = cursor.fetchall()

            connection.commit()

        connection.close()
        return data


    def TheaterDropDown(self, companyName):

        connection = get_conn()

        with connection.cursor() as cursor:

            query = """select thName from Theater
                    where comName=(%s)"""
            cursor.execute(query, (companyName))
            data=cursor.fetchall()
            connection.commit()

            connection.close()
            
            return data

    def getCreditCardNumbers(self, username):
        
        connection = get_conn()
        data = {}

        with connection.cursor() as cursor:
            
            query = """select creditCardNum from CustomerCreditCard
                    where username=(%s)"""
        
            cursor.execute(query, (username))
            data = cursor.fetchall()

        connection.close()
        return data








