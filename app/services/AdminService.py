from app.services.DBService import get_conn
import dateutil.parser

class AdminService(object):

    def ApproveUser(self,filters):

        i_username = filters.get('i_username')
        connection = get_conn()

        with connection.cursor() as cursor:
            query1 = "update User set status = 'Approved' where username = (%s)"
            cursor.execute(query1, (i_username))
            data1 = cursor.fetchall()
            connection.commit()
        connection.close()

    def DeclineUser(self,filters):

        i_username = filters.get('i_username')
        connection = get_conn()

        with connection.cursor() as cursor:
            query4 = "update User set Status = 'Declined' where username = (%s)"
            cursor.execute(query4, (i_username))
            data1 = cursor.fetchall()
            connection.commit()

        connection.close()

    def FilterUser(self, filters):

        i_username = filters.get('username')
        i_status = filters.get("i_status")
        i_sortBy = filters.get("i_sortBy")
        i_sortDirection = filters.get("i_sortDirection")
        connection = get_conn()

        with connection.cursor() as cursor:
            query =  """select * from
             (select user.username, count(CustomerCreditCard.creditCardNum) as \"creditCardNum\", user.status
             from user
             inner join CustomerCreditCard on user.username = CustomerCreditCard.username group by User.username
             union
             select user.username, 0 as \"creditCardCount\", user.status
             from user where user.username not in (select username from  CustomerCreditCard)) as Table1
             natural join
             (select user.username, \"Manager-Customer\" as \"userType\"
             from user
             where user.username in
             (select manager.username
             from manager
             inner join customer
             where manager.username=customer.username)
             union
             select user.username, \"Customer\" as \"userType\"
             from user
             where user.username in
             (select customer.username from customer)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             union
             select user.username, \"Manager\" as \"userType\"
             from user
             where user.username in
             (select manager.username from manager)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             union
             select user.username, \"User\" as \"userType\"
             from user
             where user.username in
             (select user.username from user)
             and user.username not in
             (select manager.username
             from manager
             inner join customer
             where manager.username = customer.username)
             and user.username not in (select customer.username from customer)
             and user.username not in (select manager.username from manager)) as Table2
             where (Table1.status = NULL or NULL is NULL) AND
             (Table1.username = NULL or NULL is NULL)
             ORDER BY
                  CASE WHEN @OrderDirection = \'desc\' or @OrderDirection = NULL THEN 1
                  ELSE
                       CASE WHEN @OrderByColumn = NULL THEN Table1.username
                            WHEN @OrderByColumn = \'username\' THEN Table1.username
                            WHEN @OrderByColumn = \'creditCardCount\' THEN Table1.creditCardNum
                            WHEN @OrderByColumn = \'userType\' THEN Table2.userType
                            WHEN @OrderByColumn = \'status\' THEN Table1.status
                       END
                  END DESC,
                  CASE WHEN @OrderDirection = \'asc\' THEN 1
                  ELSE
                       CASE WHEN @OrderByColumn = NULL THEN Table1.username
                            WHEN @OrderByColumn = \'username\' THEN Table1.username
                            WHEN @OrderByColumn = \'creditCardCount\' THEN Table1.creditCardNum
                            WHEN @OrderByColumn = \'userType\' THEN Table2.userType
                            WHEN @OrderByColumn = \'status\' THEN Table1.status
                       END
                  END ASC """

            cursor.execute(query, (i_username, i_username, i_status, i_status, i_sortBy, i_sortDirection))
            data = cursor.fetchall()
            connection.commit()

        connection.close()

        return data




    def ManageCompany(self, filters):

        i_comName = filters.get("i_comName")
        i_minCity = filters.get("i_minCity")
        i_maxCity = filters.get("i_maxCity")
        i_minTheater = filters.get("i_minTheater")
        i_maxTheater = filters.get("i_maxTheater")
        i_minEmployee = filters.get("i_minEmployee")
        i_maxEmployee = filters.get("i_maxEmployee")

        data_tuple = (
                    i_comName,
                    i_comName,
                    i_minCity,
                    i_minCity,
                    i_maxCity,
                    i_maxCity,
                    i_minTheater,
                    i_minTheater,
                    i_maxTheater,
                    i_maxTheater,
                    i_minEmployee,
                    i_minEmployee,
                    i_maxEmployee,
                    i_maxEmployee,
                    i_comName,
                    i_comName,
                    i_minCity,
                    i_minCity,
                    i_maxCity,
                    i_maxCity,
                    i_minTheater,
                    i_minTheater,
                    i_maxTheater,
                    i_maxTheater,
                    i_minEmployee,
                    i_minEmployee,
                    i_maxEmployee,
                    i_maxEmployee
        )


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

            cursor.execute(query, data_tuple)
            info = cursor.fetchall()
            connection.commit()


        connection.close()
        return {'ok':True, 'data':info}



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
        i_comName = filters.get("i_comName")

        with self.connection.cursor() as cursor:
            #returns all employees and the company name
            query1 = "select user.firstname, user.lastname, manager.comName from user join manager on user.username=manager.username \
            where user.username in (select manager.username from manager) and manager.comName in (select company.comName from company where company.comName = (%s))"

            cursor.execute(query1, (i_comName))
            employees = cursor.fetchall()
            self.connection.commit()
            #returns theater details for the company
            query2 = "select theater.thName, user.firstname, user.lastname, theater.thCity, theater.thState, theater.capacity \
            from theater join user on user.username=theater.manUsername where theater.comName=(%s)"


            cursor.execute(query2, (i_comName))
            theaters = cursor.fetchall()
            self.connection.commit()

        return employees
        return theaters




    def CreateMovie(self, username):

        i_adminUsername = username
        # i_movName = filters.get("i_movName")
        # i_movDuration = filters.get("i_movDuration")
        # i_movReleaseDate = filters.get("i_movReleaseDate")

        connection = get_conn()
        with connection.cursor() as cursor:


            query3 = "insert into Movie (movName, movReleaseDate, duration) \
            values ((%s), (%s), (%s))"

            cursor.execute(query3, (i_movName, i_movReleaseDate, i_duration))
            data3 = cursor.fetchall()
            connection.commit()

        connection.close()
