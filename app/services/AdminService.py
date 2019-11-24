from app.services.DBService import get_conn


class AdminService(object):

    def ApproveUser(self, username, filters):

        i_username = username
        connection = get_conn()

        with connection.cursor() as cursor:
            query1 = "update User set Status = \"Approved\" where username = (%s)"
            cursor.execute(query1, (i_username))
            data1 = cursor.fetchall()
            connection.commit()
        connection.close()

    def DeclineUser(self, username, filters):

        i_username = username
        connection = get_conn()

        with connection.cursor() as cursor:
            query4 = "update User set Status = \"Declined\" where username = (%s)"
            cursor.execute(query4, (i_username))
            data1 = cursor.fetchall()
            connection.commit()

        connection.close()

    def FilterUser(self, username, filters):

        i_username = username
        i_status = filters.get("i_status")
        i_sortBy = filters.get("i_sortBy")
        i_sortDirection = filters.get("i_sortDirection")
        connection = get_conn()

        with connection.cursor() as cursor:
            query = "select * from \
            (select user.username as \"Username\", count(CustomerCreditCard.creditCardNum) as \"Credit Card Count\", user.Status from user inner join CustomerCreditCard on user.username = CustomerCreditCard.username group by User.username \
            union \
            select user.username as \"Username\", 0 as \"Credit Card Count\", user.Status from user where user.username not in (select username from  CustomerCreditCard)) as Table1 \
            natural join \
            (select user.username as \"Username\", \"Manager-Customer\" as \"User Type\" from user where user.username in (select manager.username from manager inner join customer where manager.username=customer.username) \
            union \
            select user.username as \"Username\", \"Customer\" as \"User Type\" from user where user.username in (select customer.username from customer) and user.username not in (select manager.username from manager inner join customer where manager.username = customer.username) \
            union \
            select user.username as \"Username\", \"Manager\" as \"User Type\" from user where user.username in (select manager.username from manager) and user.username not in (select manager.username from manager inner join customer where manager.username = customer.username) \
            union \
            select user.username as \"Username\", \"User\" as \"User Type\" from user where user.username in (select user.username from user) and user.username not in (select manager.username from manager inner join customer where manager.username = customer.username) and user.username not in (select customer.username from customer) and user.username not in (select manager.username from manager)) as Table2 \
            where ((%s) is null or user.username = (%s)) AND \
            (user.status = (%s) or (%s) = "ALL") \
            order by (%s) (%s)"

            cursor.execute(query, (i_username, i_username, i_status, i_status, i_sortBy, i_sortDirection))
            data = cursor.fetchall()
            connection.commit()

        connection.close()


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

        connection = get_conn()
        with connection.cursor() as cursor:
            query = "select manager.comName as \"Company\", count(distinct theater.thCity) as \"City Count\", \
            count(distinct theater.thName) \"Theater Count\", count(distinct Manager.username) as \"Employee Count\" \
            from theater join Manager on theater.comName=Manager.comName group by theater.comName  \
            where ((%s) is Null or Manager.comName = (%s)),\
            and (where (%s) is Null or count(distinct theater.thCity)>=(%s)),\
            and (where (%s) is Null or count(distinct theater.thCity)<=(%s)),\
            and (where (%s) is Null or count(distinct theater.thName)>=(%s)),\
            and (where (%s) is Null or count(distinct theater.thName)<=(%s)),\
            and (where (%s) is Null or count(distinct manager.username)>=(%s)),\
            and (where (%s) is Null or count(distinct manager.username)<=(%s)),\
            union select company.comName as \"Company\", 0 as \"City Count\", 0 as \"Theater Count\",\
            0 as \"Employee Count\" from company where company.comName not in (select Manager.comName from\
            Manager) and\
            where (%s) is Null or Manager.comName = (%s),\
            and (where (%s) is Null or count(distinct theater.thCity)>=0),\
            and (where (%s) is Null or count(distinct theater.thCity)<=0),\
            and (where (%s) is Null or count(distinct theater.thName)>=0),\
            and (where (%s) is Null or count(distinct theater.thName)<=0),\
            and (where (%s) is Null or count(distinct manager.username)>=0),\
            and (where (%s) is Null or count(distinct manager.username)<=0)"

            data = cursor.execute(query, (i_comName,i_comName,i_minCity,i_minCity,i_maxCity,i_maxCity,i_minTheater,i_minTheater,i_maxTheater,i_maxTheater,i_minEmployee,i_minEmployee,i_maxEmployee,i_maxEmployee,i_comName,i_comName,i_minCity,i_minCity,i_maxCity,i_maxCity,i_minTheater,i_minTheater,i_maxTheater,i_maxTheater,i_minEmployee,i_minEmployee,i_maxEmployee,i_maxEmployee))
            info = cursor.fetchall()
            connection.commit()
            return info

        connection.close()



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

        connection = get_conn()
        with connection.cursor() as cursor:

            query2 = "insert into Theater (thName, comName, capacity, thStreet, thCity, thState, thZipcode, manUsername) \
            values ((%s), (%s), (%s), (%s), (%s), (%s), (%s), (%s))"

            cursor.execute(query2, (i_thName, i_comName, i_capacity, i_thStreet, i_thCity, i_thState, i_thZipcode, i_manUsername))
            data2 = cursor.fetchall()
            connection.commit()

        connection.close()

    def CompanyDetail(self, username, filters):



    def CreateMovie(self, username, filters):

        i_adminUsername = username
        i_movName = filters.get("i_movName")
        i_movDuration = filters.get("i_movDuration")
        i_movReleaseDate = filters.get("i_movReleaseDate")

        connection = get_conn()
        with connection.cursor() as cursor:

            query3 = "insert into Movie (movName, movReleaseDate, duration) \
            values ((%s), (%s), (%s))"

            cursor.execute(query3, (i_movName, i_movReleaseDate, i_duration))
            data3 = cursor.fetchall()
            connection.commit()
