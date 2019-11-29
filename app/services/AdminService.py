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
            query4 = """update User set Status = 'Declined' where status='Pending'
            and username = (%s)"""
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
             where (Table1.status = (%s) or (%s) is NULL) AND
             (Table1.username = (%s) or (%s) is NULL or (%s) = "")
             ORDER BY
                  CASE WHEN (%s) = \'desc\' or (%s) = NULL THEN 1
                  ELSE
                       CASE WHEN (%s) = NULL THEN Table1.username
                            WHEN (%s) = \'username\' THEN Table1.username
                            WHEN (%s) = \'creditCardCount\' THEN Table1.creditCardNum
                            WHEN (%s) = \'userType\' THEN Table2.userType
                            WHEN (%s) = \'status\' THEN Table1.status
                       END
                  END DESC,
                  CASE WHEN (%s) = \'asc\' THEN 1
                  ELSE
                       CASE WHEN (%s) = NULL THEN Table1.username
                            WHEN (%s) = \'username\' THEN Table1.username
                            WHEN (%s) = \'creditCardCount\' THEN Table1.creditCardNum
                            WHEN (%s) = \'userType\' THEN Table2.userType
                            WHEN (%s) = \'status\' THEN Table1.status
                       END
                  END ASC """
            cursor.execute(query, (i_status, i_status, i_username, i_username, i_username, i_sortDirection, i_sortDirection, i_sortBy, i_sortBy, i_sortBy, i_sortBy, i_sortBy, i_sortDirection, i_sortBy, i_sortBy, i_sortBy, i_sortBy, i_sortBy))
            data = cursor.fetchall()
            connection.commit()

        connection.close()

        return data




    def ManageCompany(self, filters):
        if(filters.get("i_comName") != None):
            i_comName = filters.get("i_comName")["value"]
        else:
            i_comName = ""

        i_minCity = filters.get("i_minCity")
        i_maxCity = filters.get("i_maxCity")
        i_minTheater = filters.get("i_minTheater")
        i_maxTheater = filters.get("i_maxTheater")
        i_minEmployee = filters.get("i_minEmployee")
        i_maxEmployee = filters.get("i_maxEmployee")
        i_sortBy = filters.get("i_sortBy")
        i_sortDirection = filters.get("i_sortDirection")
        

        data_tuple = (
                    i_comName,
                    i_comName,
                    i_comName,
                    i_minCity, # line 185
                    i_minCity,
                    i_maxCity, # line 186
                    i_maxCity,
                    i_minTheater,
                    i_minTheater,
                    i_maxTheater, #line 189
                    i_maxTheater,
                    i_minEmployee,
                    i_minEmployee,
                    i_maxEmployee,
                    i_maxEmployee,
                    i_sortDirection, # line 193
                    i_sortDirection,
                    i_sortBy, # line 195
                    i_sortBy,
                    i_sortBy, # line 197
                    i_sortBy,
                    i_sortBy,
                    i_sortDirection, #line 202
                    i_sortBy,
                    i_sortBy,
                    i_sortBy,
                    i_sortBy,
                    i_sortBy,
        )









        connection = get_conn()


        with connection.cursor() as cursor:

            query = """select manager.comName as "comName", count(distinct theater.thCity) as "numCityCover",
            count(distinct theater.thName) as "numTheater", count(distinct Manager.username) as "numEmployee"
            from theater join Manager on theater.comName = Manager.comName group by theater.comName
            having
            (i_comName%s = "ALL" or i_comName%s = "" or manager.comName = i_comName%s)
            and (count(distinct theater.thCity) >= i_minCity%s or i_minCity%s is NULL)
            and (count(distinct theater.thCity) <= i_maxCity%s or i_maxCity%s is NULL)
            and (count(distinct theater.thName) >= i_minTheater%s or i_minTheater%s is NULL)
            and (count(distinct theater.thName) <= i_maxTheater%s or i_maxTheater%s is NULL)
            and (count(distinct Manager.username) >= i_minEmployee%s or i_minEmployee%s is NULL)
            and (count(distinct Manager.username) <= i_maxEmployee%s or i_maxEmployee%s is NULL)
            ORDER BY
                  CASE WHEN i_sortDirection%s = 'DESC' or i_sortDirection%s = '' THEN 1
                  ELSE
                       CASE WHEN i_sortBy%s = '' THEN manager.comName
                            WHEN i_sortBy%s = 'comName' THEN manager.comName
                            WHEN i_sortBy%s = 'numCityCover' THEN count(distinct theater.thCity)
                            WHEN i_sortBy%s = 'numTheater' THEN count(distinct theater.thName)
                            WHEN i_sortBy%s = 'numEmployee' THEN count(distinct Manager.username)
                       END
                  END ASC,
                  CASE WHEN i_sortDirection%s = 'ASC' THEN 1
                  ELSE
                       CASE WHEN i_sortBy%s = '' THEN manager.comName
                            WHEN i_sortBy%s = 'comName' THEN manager.comName
                            WHEN i_sortBy%s = 'numCityCover' THEN count(distinct theater.thCity)
                            WHEN i_sortBy%s = 'numTheater' THEN count(distinct theater.thName)
                            WHEN i_sortBy%s = 'numEmployee' THEN count(distinct Manager.username)
                       END
                  END DESC;"""

            cursor.execute(query, data_tuple)
            info = cursor.fetchall()
            connection.commit()


        connection.close()
        return {'ok':True, 'data':info}



    def CreateTheater(self, filters):

        i_thName = filters.get("i_thName")
        i_comName = filters.get("i_comName")
        i_thStreet = filters.get("i_thStreet")
        i_thCity = filters.get("i_thCity")
        i_thState = filters.get("i_thState")
        i_thZipcode = filters.get("i_thZipcode")
        i_capacity = filters.get("i_capacity")
        i_manUsername = filters.get("i_manUsername")

        if i_thState == "ALL":
          raise Exception("State Cannot Be ALL")

        connection = get_conn()
        with connection.cursor() as cursor:


            query2 = "insert into Theater (thName, comName, capacity, thStreet, thCity, thState, thZipcode, manUsername) \
            values ((%s), (%s), (%s), (%s), (%s), (%s), (%s), (%s))"

            cursor.execute(query2, (i_thName, i_comName, i_capacity, i_thStreet, i_thCity, i_thState, i_thZipcode, i_manUsername))
            
            connection.commit()

        connection.close()
        

    def CompanyDetail(self, comName):
        i_comName = comName

        connection = get_conn()
        with connection.cursor() as cursor:
            #returns all employees and the company name
            query1 = """select user.firstname, user.lastname, manager.comName from user
            join manager on user.username=manager.username 
            where user.username in 
            (select manager.username from manager) 
            and manager.comName in 
            (select company.comName from company where company.comName = (%s))"""

            cursor.execute(query1, (i_comName))
            employees = cursor.fetchall()
            connection.commit()
            #returns theater details for the company
            query2 = "select theater.thName, user.firstname, user.lastname, theater.thCity, theater.thState, theater.capacity \
            from theater join user on user.username=theater.manUsername where theater.comName=(%s)"


            cursor.execute(query2, (i_comName))
            theaters = cursor.fetchall()
            connection.commit()

        return {"ok":True, "employees":employees, "theaters":theaters}



    def CreateMovie(self, filters):

        i_movName = filters.get("movieName")
        i_movDuration = filters.get("duration")

        i_movReleaseDate = (dateutil.parser.parse(filters.get("releaseDate"))).date()



        connection = get_conn()
        with connection.cursor() as cursor:

            query7 = "SELECT movName FROM Movie WHERE (movName=(%s)) AND (movReleaseDate=(%s))"
            cursor.execute(query7, (i_movName, i_movReleaseDate))
            data = cursor.fetchall()
            connection.commit()
            print(data)
            if len(data) < 1:
                query3 = "insert into Movie (movName, movReleaseDate, duration) \
                values ((%s), (%s), (%s))"

                cursor.execute(query3, (i_movName, i_movReleaseDate, i_movDuration))
                connection.commit()
            else:
                connection.close()
                return("Movie name and release date combination already taken")

        connection.close()
        return("Movie Registered")
