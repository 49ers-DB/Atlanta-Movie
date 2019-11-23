
class DropDownService(object):

    def __init__(self, connection):
        self.connection = connection


    def CompanyDropDown(self):

        with self.connection.cursor() as cursor:
    #Manager-Only Registration, Manager-Customer Registration, Manage Company, Create Theater
    # Explore Movie, Explore Theater, Visit History

            query = "select comName from Company"


    def ManagerDropDown(self):

        with self.connection.cursor() as cursor:
    #Create Theater

            query = "select firstname, lastname from User inner join Manager on Manager.username = User.username"


    def MovieDropDown(self):

        with self.connection.cursor() as cursor:
    #Schedule Movie, Explore Movie

            query = "select movName from Movie"


    def TheaterDropDown(self):

        with self.connection.cursor() as cursor:
    #Explore Theater

            query = "select thName from Theater"






