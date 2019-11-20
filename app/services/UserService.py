class UserService(object):

    def __init__(self, connection):
        self.connection = connection

    def ExploreTheater(self, username, filters):
        i_thname=filters.get("i_thname")
        i_coname=filters.get("i_coname")
        i_city=filters.get("i_city")
        i_state=filters.get("i_state")

        with self.connection.cursor() as cursor:
            info = "select distinct thName as \"Name\", thStreet as \"Street\", thCity as \"City\", thState as \"State\", thZipcode as \"Zipcode\", comName as \"Company\" from \
            Theater where ((%s) is NULL or thName = (%s)) \
            and ((%s) is NULL or thCity = (%s)) \
            and ((%s) is NULL or thCity = (%s)) \
            and ((%s) is NULL or thCity = (%s))"

            cursor.execute(info,(i_thname,i_coname,i_city,i_state))
            data=cursor.fetchall()
            self.connection.commit()

    def LogVisit(self, username, filters):
        i_thname=filters.get("i_thname")
        i_coname=filters.get("i_coname")
        i_visitdate=filters.get("i_visitdate")
        i_username = username

        with self.connection.cursor() as cursor:
            leng="select visitID from UserVisitTheater"
            cursor.execute(leng)
            length=cursor.fetchall()
            self.connection.commit()
            new_id= int(len(length.values()))+1
            info="insert (visitID,username,thName,comName,visitDate) values ((%s),(%s),(%s),(%s),(%s))"
            cursor.execute(info,(new_id,i_username,i_thname,i_coname,i_visitdate))
            data=cursor.fetchall()
            self.connection.commit()

    def VisitHistory(self, username, filters):
        i_coname=filters.get("i_coname")
        i_minvisitdate =filters.get("i_minvisitdate")
        i_maxvisitdate =filters.get("i_maxvisitdate")
        i_username = username
'''
        with self.connection.cursor() as cursor:
            info="select thName, thStreet, thCity, thState, thZipcode, comName, visitDate from UserVisitTheater natural join Theater where (username = i_username) and (i_minVisitDate IS null or visitDate >= i_minVisitDate) and (i_maxVisitDate is null or visitDate <= i_maxVisitDate)"

'''

