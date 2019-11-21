
class AdminService(object):

    def __init__(self, connection):
        self.connection = connection

    def ApproveUser(self, username, filters):

        i_username = username

    with self.connection.cursor()
        query1 = "update User set Status = \"Approved\" where username = (%s)"
        cursor.execute(query1, (i_username))
        data1 = cursor.fetchall()
        self.connection.commit()

    def DeclineUser(self, username, filters):

        i_username = username

    with self.connection.cursor()
        query4 = "update User set Status = \"Declined\" where username = (%s)"
        cursor.execute(query4, (i_username))
        data1 = cursor.fetchall()
        self.connection.commit()

    def ManageCompany(self, username, filters):

        i_adminUsername = username
        i_comName = filters.get("i_comName")
        i_minCity = filters.get("i_minCity")
        i_maxCity = filters.get("i_maxCity")
        i_minTheater = filters.get("i_minTheater")
        i_maxTheater = filters.get("i_maxTheater")
        i_minEmployee = filters.get("i_minEmployee")
        i_maxEmployee = filters.get("i_maxEmployee")
        i_sortBy
        i_sortDirection

    with self.connection.cursor() as cursor:
        query = "select comName, count(thName), count(thCity), count(manUsername) \
        from theater \
        where (comName = (%s) or (%s) is NULL) AND \
        \
        group by comName"


    def CreateTheater(self, username, filters):

        i_adminUsername = username
        i_thName = filters.get("i_thName")
        i_comName = filters.get("i_comName")
        i_thStreet = filters.get("i_thStreet")
        i_thCity = filters.get("i_thCity")
        i_thState = filters.get("i_thState")
        i_thZipcode = filters.get("i_thZipcode")
        i_capacity = filters.get("i_capacity")
        i_manUsername = filters.get("i_manUsername")

    with self.connection.cursor() as cursor:

        query2 = "insert into Theater (thName, comName, capacity, thStreet, thCity, thState, thZipcode, manUsername) \
        values ((%s), (%s), (%s), (%s), (%s), (%s), (%s), (%s))"

        cursor.execute(query2, (i_thName, i_comName, i_capacity, i_thStreet, i_thCity, i_thState, i_thZipcode, i_manUsername))
        data2 = cursor.fetchall()
        self.connection.commit()


    def CompanyDetail(self, username, filters):



    def CreateMovie(self, username, filters):

        i_adminUsername = username
        i_movName = filters.get("i_movName")
        i_movDuration = filters.get("i_movDuration")
        i_movReleaseDate = filters.get("i_movReleaseDate")

    with self.connection.cursor() as cursor:

        query3 = "insert into Movie (movName, movReleaseDate, duration) \
        values ((%s), (%s), (%s))"

        cursor.execute(query3, (i_movName, i_movReleaseDate, i_duration))
        data3 = cursor.fetchall()
        self.connection.commit()











