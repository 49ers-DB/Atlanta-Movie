from app.services.DBService import get_conn




class UserService(object):

   
    def ExploreTheater(self, filters):
        i_thname=filters.get("selectedTheater")
        i_coname=filters.get("selectedCompany")
        i_city=filters.get("city")
        i_state=filters.get("selectedState")

        data_tuple = (
            i_thname,
            i_thname,
            i_coname,
            i_coname,
            i_city,
            i_city,
            i_state,
            i_state)

        connection = get_conn()
        with connection.cursor() as cursor:
            info = "select distinct thName as \"Name\", thStreet as \"Street\", thCity as \"City\", thState as \"State\", thZipcode as \"Zipcode\", comName as \"Company\" from \
            Theater where ((%s) is NULL or thName = (%s)) \
            and ((%s) is NULL or thCity = (%s)) \
            and ((%s) is NULL or thCity = (%s)) \
            and ((%s) is NULL or thCity = (%s))"


            cursor.execute(info, data_tuple)
            data=cursor.fetchall()
            connection.commit()

        connection.close()
        print(data)
        return data

    def LogVisit(self, username, filters):
        i_thname=filters.get("i_thname")
        i_coname=filters.get("i_coname")
        i_visitdate=filters.get("i_visitdate")
        i_username = username

        connection = get_conn()
        with connection.cursor() as cursor:
            leng="select visitID from UserVisitTheater"
            cursor.execute(leng)
            length=cursor.fetchall()
            connection.commit()
            new_id= int(len(length.values()))+1
            info="insert (visitID,username,thName,comName,visitDate) values ((%s),(%s),(%s),(%s),(%s))"
            cursor.execute(info,(new_id,i_username,i_thname,i_coname,i_visitdate))
            data=cursor.fetchall()
            connection.commit()

        connection.close()

    def VisitHistory(self, username, filters):
        i_comName=filters.get("i_comName")
        i_minVisitDate =filters.get("i_minVisitDate")
        i_maxVisitDate =filters.get("i_maxVisitDate")
        i_username = username

        connection = get_conn()

        with connection.cursor() as cursor:


            info = "select Theater.thName, Theater.thStreet, Theater.thCity, Theater.thState, Theater.thZipcode, Theater.comName, UserVisitTheater.visitDate\
            from UserVisitTheater natural join Theater \
            where (username = (%s)) and ((%s) is null or UserVisitTheater.visitDate >= (%s)) and ((%s) is null or UserVisitTheater.visitDate <= (%s)) and ((%s) is null or Theater.comName = (%s))"

            cursor.execute(info, (i_username, i_minVisitDate, i_minVisitDate, i_maxVisitDate, i_maxVisitDate, i_comName, i_comName))
            data = cursor.fetchall()
            connection.commit()

        connection.close()
        return data
