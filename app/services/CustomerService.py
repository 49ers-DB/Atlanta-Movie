from app.services.DBService import get_conn
import dateutil.parser

class CustomerService(object):

    def ExploreMovie(self, filters):
        i_movName = filters.get("i_movName")
        i_comName = filters.get("i_comName")
        i_city = filters.get("i_city")
        i_state = filters.get("i_state")
        i_minMovPlayDate = filters.get("i_minMovPlayDate")
        i_maxMovPlayDate = filters.get("i_maxMovPlayDate")

        connection = get_conn()
        with connection.cursor() as cursor:

            cursor.callproc("customer_filter_mov", (i_movName, i_comName, i_city, i_state , i_minMovPlayDate, i_maxMovPlayDate, ))
            data = cursor.fetchall()
            connection.commit()

        connection.close()
        return data


    def ExploreMovie1(self, filters):

        i_movName = filters.get("i_movName")
        i_comName = filters.get("i_comName")
        i_city = filters.get("i_city")
        i_state = filters.get("i_state")
        i_minMovPlayDate = filters.get("i_minMovPlayDate")
        i_maxMovPlayDate = filters.get("i_maxMovPlayDate")

        if i_city == "":
            i_city = None

        if i_state == "":
            i_state = None

        data_tuple = (
            i_movName,
            i_movName,
            i_comName,
            i_comName,
            i_city,
            i_city,
            i_state,
            i_state,
            i_minMovPlayDate,
            i_minMovPlayDate,
            i_maxMovPlayDate,
            i_maxMovPlayDate)

        connection = get_conn()
        data = {}

        with connection.cursor() as cursor:

            query = "SELECT MoviePlay.movName, MoviePlay.comName,Theater.thName, Theater.thStreet, Theater.thCity, Theater.thState, Theater.thZipcode, MoviePlay.movPlayDate\
            FROM MoviePlay INNER JOIN Theater ON Theater.thName = MoviePlay.thName AND Theater.comName = MoviePlay.comName\
            WHERE (MoviePlay.movName = (%s) OR (%s) is NULL) AND \
            (MoviePlay.comName = (%s) OR (%s) is NULL) AND \
            (Theater.thCity = (%s) OR (%s) is NULL) AND \
            (Theater.thState = (%s) OR (%s) is NULL) AND \
            (MoviePlay.movPlayDate >= (%s) OR (%s) is NULL) AND \
            (MoviePlay.movPlayDate <= (%s) OR (%s) is NULL)"

            cursor.execute(query, data_tuple)
            data = cursor.fetchall()
            connection.commit()

        connection.close()
        return data

    def ViewMovie(self, filters):
        i_creditCardNum = filters.get("i_creditCardNum")
        i_movName = filters.get("i_movName")
        i_movPlayDate = filters.get("i_movPlayDate")
        i_thName = filters.get("i_thName")
        i_comName = filters.get("i_comName")

        i_movReleaseDate = filters.get("i_movReleaseDate")

        connection = get_conn()
        with connection.cursor() as cursor:
            if i_movReleaseDate is None:
                sql = """SELECT movReleaseDate from MoviePlay where thName=(%s) and movName=(%s) and movPlayDate=(%s) and comName=(%s)"""
                cursor.execute(sql, (i_thName, i_movName, i_movPlayDate, i_comName))
                data = cursor.fetchall()
                i_movReleaseDate = data[0]['movReleaseDate']
            
            cursor.callproc('customer_view_mov', (i_creditCardNum, i_movName, i_movReleaseDate,i_thName, i_comName, i_movPlayDate, ))
            data = cursor.fetchall()
        
        connection.commit()

        connection.close()
        return data



    def ViewMovie1(self, username, filters):

       

        i_movPlayDate = dateutil.parser.parse(i_movPlayDate)

        connection = get_conn()

        with connection.cursor() as cursor:

            query = "select movReleaseDate from MoviePlay where MoviePlay.movName = (%s)"
            cursor.execute(query, (i_movName))
            data2 = cursor.fetchall()
            connection.commit()
            movReleaseDate = data2[0]['movReleaseDate']

            query2 = """insert into CustomerViewMovie (creditCardNum, thName, comName, movName, movReleaseDate, movPlayDate)
            values ((%s), (%s), (%s), (%s), (%s), (%s))"""
            print((i_creditCardNum, i_thName, i_comName, i_movName, movReleaseDate, i_movPlayDate))
            cursor.execute(query2, (i_creditCardNum, i_thName, i_comName, i_movName, movReleaseDate, i_movPlayDate))
            data3 = cursor.fetchall()
            connection.commit()


        connection.close()

    def ViewHistory(self, filters):
        i_cusUsername = filters.get('i_cusUsername')
        connection = get_conn()

        with connection.cursor() as cursor:

            cursor.callproc('customer_view_history', (i_cusUsername,))
            history = cursor.fetchall()
            connection.commit()

        connection.close()
        return history

    def ViewHistory1(self, username):

        i_cusUsername = username
        connection = get_conn()

        with connection.cursor() as cursor:

            query2 = "select movName, thName, comName, creditCardNum, movPlayDate \
            from CustomerViewMovie \
            where CustomerViewMovie.creditCardNum in (select creditCardNum from CustomerCreditCard where CustomerCreditCard.username = (%s))"

            cursor.execute(query2, i_cusUsername)
            data3 = cursor.fetchall()
            connection.commit()

        connection.close()
        return data3



