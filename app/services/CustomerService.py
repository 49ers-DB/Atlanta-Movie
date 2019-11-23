import DBService


class CustomerService(object):


    def ExploreMovie(self, username, filters):

        i_username = username
        i_movName = filters.get("i_movName")
        i_comName = filters.get("i_comName")
        i_city = filters.get("i_city")
        i_state = filters.get("i_state")
        i_minMovPlayDate = filters.get("i_minMovPlayDate")
        i_maxMovPlayDate = filters.get("i_maxMovPlayDate")

        connection = DBService.get_conn()

        with connection.cursor() as cursor:

            query = "SELECT MoviePlay.movName, MoviePlay.comName, Theater.thStreet, Theater.thCity, Theater.thState, Theater.thZipcode, MoviePlay.movPlayDate\
            FROM MoviePlay INNER JOIN Theater ON Theater.thName = MoviePlay.thName AND Theater.comName = MoviePlay.comName\
            WHERE (MoviePlay.movName = (%s) OR (%s) is NULL) AND \
            (MoviePlay.comName = (%s) OR (%s) is NULL) AND \
            (Theater.thCity = (%s) OR (%s) is NULL) AND \
            (Theater.thState = (%s) OR (%s) is NULL) AND \
            (MoviePlay.movPlayDate >= (%s) OR (%s) is NULL) AND \
            (MoviePlay.movPlayDate <= (%s) OR (%s) is NULL)"

            cursor.execute(query, (i_movName, i_movName, i_comName, i_comName, i_city, i_city, i_state, i_state, i_minMovPlayDate, i_minMovPlayDate, i_maxMovPlayDate, i_maxMovPlayDate))
            data = cursor.fetchall()
            connection.commit()

        connection.close()

    def ViewMovie(self, username, filters):

        i_username = username
        i_creditCardNum = filters.get("i_creditCardNum")
        i_movName = filters.get("i_movName")
        i_movReleaseDate = filters.get("i_movReleaseDate")
        i_thName = filters.get("i_thName")
        i_comName = filters.get("i_comName")

        connection = DBService.get_conn()

        with connection.cursor() as cursor:

            query = "select movReleaseDate MoviePlay where MoviePlay.movName = (%s)"
            cursor.execute(query, (i_movName))
            data2 = cursor.fetchall()
            connection.commit()

            query2 = "insert into CustomerViewMovie (creditCardNum, thName, comName, movName, movReleaseDate, movPlayDate) \
            values ((%s), (%s), (%s), (%s), (%s), (%s))"
            cursor.execute(query2, (i_creditCardNum, i_thName, i_comName, i_movName, data2[movReleaseDate], i_movPlayDate))
            data3 = cursor.fetchall()
            connection.commit()

        connection.close()


    def ViewHistory(self, username, filters):

        i_cusUsername = username
        connection = DBService.get_conn()

        with connection.cursor() as cursor:

            query2 = "select movName, thName, comName, creditCardNum, movPlayDate \
            from CustomerViewMovie \
            where CustomerViewMovie.creditCardNum in (select creditCardNum from CustomerCreditCard where CustomerCreditCard.username = (%s))"

            cursor.execute(query2, i_cusUsername)
            data3 = cursor.fetchall()
            connection.commit()

        connection = DBService.get_conn()



