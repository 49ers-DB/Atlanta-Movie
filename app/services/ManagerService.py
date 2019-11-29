from app.services.DBService import get_conn
import dateutil.parser

class ManagerService(object):

    def TheaterOverview(self, username, filters):

        i_username = username
        i_minReleaseDate=filters.get("i_minReleaseDate")
        i_maxReleaseDate=filters.get("i_maxReleaseDate")
        i_minPlayDate=filters.get("i_minPlayDate")
        i_maxPlayDate=filters.get("i_maxPlayDate")
        i_minDuration=filters.get("i_minDuration")
        i_maxDuration=filters.get("i_maxDuration")
        i_Movie=filters.get("i_Movie")
        i_notplayed=filters.get("i_notplayed")

        if i_Movie == "":
            i_Movie = None
        
        if i_minDuration == "":
            i_minDuration = None

        if i_maxDuration == "":
            i_maxDuration = None

        data_tuple = (i_username,
                i_minReleaseDate,
                i_minReleaseDate,
                i_maxReleaseDate,
                i_maxReleaseDate,
                i_maxPlayDate,
                i_maxPlayDate,
                i_minPlayDate,
                i_minPlayDate,
                i_maxDuration,
                i_maxDuration,
                i_minDuration,
                i_minDuration,
                i_Movie,
                i_Movie,
                i_notplayed,
                i_minReleaseDate,
                i_minReleaseDate,
                i_maxReleaseDate,
                i_maxReleaseDate,
                i_minDuration,
                i_minDuration,
                i_maxDuration,
                i_maxDuration,
                i_Movie,
                i_Movie)

        connection = get_conn()

        with connection.cursor() as cursor:

            info = """select distinct MoviePlay.movName as \"Movie\", MoviePlay.movReleaseDate as \"Release_Date\",
            MoviePlay.movPlayDate as \"Play_Date\", Movie.duration as \"Duration\"
            from MoviePlay join Movie on MoviePlay.movName=Movie.movName where MoviePlay.thName in
            (select thName from Theater where Theater.manUsername=(%s))
            and ((%s) is NULL or Movie.movReleaseDate >=(%s))
            and ((%s) is NULL or Movie.movReleaseDate <=(%s))
            and ((%s) is NULL or MoviePlay.movPlayDate <=(%s))
            and ((%s) is NULL or MoviePlay.movPlayDate >=(%s))
            and ((%s) is NULL or Movie.duration <=(%s))
            and ((%s) is NULL or Movie.duration >=(%s))
            and ((%s) is NULL or Movie.movName like(%s))
            and ((%s) is NULL or MoviePlay.movPlayDate!=NULL)
            Union
            select Movie.movName as \"Movie\", Movie.movReleaseDate as \"Release_Date\",
            cast(NULL as date) as \"Play_Date\", Movie.duration as \"Duration\" from Movie
            where ((%s) is NULL or Movie.movReleaseDate >=(%s))
            and ((%s) is NULL or Movie.movReleaseDate <=(%s))
            and ((%s) is NULL or Movie.duration >=(%s))
            and ((%s) is NULL or Movie.duration <=(%s))
            and ((%s) is NULL or Movie.movName like(%s))"""

            cursor.execute(info, data_tuple)
            data=cursor.fetchall()
            connection.commit()

            connection.close()

        return data


    def ScheduleMovie(self, username, filters):

        i_manUsername = username
        i_movName = filters.get("i_movName")
        i_movReleaseDate = filters.get("i_movReleaseDate")
        i_movPlayDate = filters.get("i_movPlayDate")
        connection = get_conn()

        i_movPlayDate = dateutil.parser.parse(i_movPlayDate).date()
        i_movReleaseDate = dateutil.parser.parse(i_movReleaseDate).date()

        if i_movPlayDate < i_movReleaseDate:
            raise Exception("Movie play date Cannot be scheduled before Movie Release Date")

        with connection.cursor() as cursor:

            query = cursor.execute("select movName, movReleaseDate from Movie") # movieSchedule1 is the output for Schedule Movie
            movieSchedule1 = cursor.fetchall()
            connection.commit()

            query = "select thName, comName, capacity from Theater where manUsername = (%s)"
            cursor.execute(query, (i_manUsername))
            data2 = cursor.fetchall()[0]
            connection.commit()

            query = """SELECT count(*) as 'numScheduled' FROM MoviePlay
                where thName in (SELECT thName FROM Theater where Theater.manUsername = (%s))
                and comName in (SELECT comName FROM Theater where Theater.manUsername = %s)
                and movPlayDate=%s;"""
            cursor.execute(query, (i_manUsername, i_manUsername, i_movPlayDate))
            data = cursor.fetchall()
            numScheduled = data[0]['numScheduled']

            print(numScheduled, data2,['capacity'])

            if data2['capacity'] <= numScheduled:
                raise Exception("Scheduling this movie would exceed Theater capacity")

            query = "insert into MoviePlay (thName, comName, movName, movReleaseDate, movPlayDate) values ((%s), (%s), (%s), (%s), (%s))"
            cursor.execute(query, (data2['thName'], data2['comName'], i_movName, i_movReleaseDate, i_movPlayDate))
            data3 = cursor.fetchall()
            connection.commit()

        connection.close()








