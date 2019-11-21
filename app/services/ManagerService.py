

class ManagerService(object):

    def __init__(self, connection):
        self.connection = connection

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

        with self.connection.cursor() as cursor:


            info = "select distinct MoviePlay.movName as \"Movie\", MoviePlay.movReleaseDate as \"Release_Date\", \
            MoviePlay.movPlayDate as \"Play_Date\", Movie.duration as \"Duration\" from MoviePlay  \
            join Movie on MoviePlay.movName=Movie.movName \
            where MoviePlay.thName in (select thName from Theater where Theater.manUsername=(%s)) \
            and ((%s) is not NULL and Movie.movReleaseDate >= (%s)) \
            and ((%s) is not NULL and Movie.movReleaseDate <= (%s)) \
            and ((%s) is not NULL and MoviePlay.movPlayDate <= (%s)) \
            and ((%s) is not NULL and MoviePlay.movPlayDate >= (%s)) \
            and ((%s) is not NULL and Movie.movName = (%s)) \
            and ((%s) = FALSE and MoviePlay.movPlayDate is not NULL)\
            Union \
            select Movie.movName as \"Movie\", Movie.movReleaseDate as \"Release_Date\", cast(NULL as date) as \"Play_Date\", Movie.duration as \"Duration\" from Movie\
            where ((%s) is not NULL and Movie.movReleaseDate >= (%s)) \
            and ((%s) is not NULL and Movie.movReleaseDate <= (%s)) \
            and ((%s) is not NULL and Movie.Duration <= (%s)) \
            and ((%s) is not NULL and Movie.Duration >= (%s))\
            and ((%s) is not NULL and Movie.movName = (%s))"



            cursor.execute(info, (i_username, i_minReleaseDate, i_minReleaseDate, i_maxReleaseDate,i_maxReleaseDate, i_maxPlayDate,i_maxPlayDate, i_minPlayDate,i_minPlayDate,
                i_Movie, i_Movie,i_notplayed,i_minReleaseDate, i_minReleaseDate, i_maxReleaseDate,i_maxReleaseDate,i_maxDuration, i_maxDuration,i_minDuration, i_minDuration,i_Movie, i_Movie))
            data=cursor.fetchall()
            self.connection.commit()


def ScheduleMovie(self, username, filters):

        i_manUsername = username

        i_movName = filters.get("i_movName")

        i_movReleaseDate = filters.get("i_movReleaseDate")

        i_movPlayDate = filters.get("i_movPlayDate")

        with self.connection.cursor() as cursor:

            query = cursor.execute("select movName, movReleaseDate from Movie") # movieSchedule1 is the output for Schedule Movie

            movieSchedule1 = cursor.fetchall()

            self.connection.commit()

            query = "select thName, comName from Theater where manUsername = (%s)"

            cursor.execute(query, (i_manUsername))

            data2 = cursor.fetchall()

            self.connection.commit()

            query = "insert into MoviePlay (thName, comName, movName, movReleaseDate, movPlayDate) values ((%s), (%s), (%s), (%s), (%s))"

            cursor.execute(query, (data2[thName], data2[comName], i_movName, i_movReleaseDate, i_movPlayDate))

            data3 = cursor.fetchall()

            self.connection.commit()





