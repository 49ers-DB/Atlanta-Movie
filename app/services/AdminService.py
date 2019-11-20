
class AdminService(object):

    def __init__(self, connection):
        self.connection = connection

    def ManageUser(self, username, filters):

        i_username = username

# How do I approve or decline a user?

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



    def CompanyDetail(self, username, filters):



    def CreateMovie(self, username, filters):


