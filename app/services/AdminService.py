from app.services.DBService import get_conn
import dateutil.parser

class AdminService(object):

    def ApproveUser(self, filters):
        i_username = filters.get('i_username')
        connection = get_conn()
        
        with connection.cursor() as cursor:
            cursor.callproc("admin_approve_user", (i_username, ))

            connection.commit()
        
        connection.close()


    def DeclineUser(self,filters):

        i_username = filters.get('i_username')
        connection = get_conn()

        with connection.cursor() as cursor:
            cursor.callproc("admin_decline_user", (i_username, ))
            connection.commit()

        connection.close()

    def FilterUser(self, filters):

        i_username = filters.get('username')
        i_status = filters.get("i_status")
        i_sortBy = filters.get("i_sortBy")
        i_sortDirection = filters.get("i_sortDirection")
        connection = get_conn()

        with connection.cursor() as cursor:
            cursor.callproc("admin_filter_user", (i_username, i_status, i_sortBy, i_sortDirection,))
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
        i_sortBy = filters.get("i_sortBy")
        i_sortDirection = filters.get('i_sortDirection')


        connection = get_conn()
        with connection.cursor() as cursor:
            cursor.callproc("admin_filter_company", (i_comName, i_minCity, i_maxCity, i_minTheater, i_maxTheater, i_minEmployee, i_maxEmployee, i_sortBy,i_sortDirection,))
            info = cursor.fetchall()
            connection.commit()


        connection.close()
        return info



    def CreateTheater(self, filters):

        i_thName = filters.get("i_thName")
        i_comName = filters.get("i_comName")
        i_thStreet = filters.get("i_thStreet")
        i_thCity = filters.get("i_thCity")
        i_thState = filters.get("i_thState")
        i_thZipcode = filters.get("i_thZipcode")
        i_capacity = filters.get("i_capacity")
        i_manUsername = filters.get("i_managerUsername")

        connection = get_conn()
        with connection.cursor() as cursor:
            print((i_thName, i_comName, i_thStreet, i_thCity, i_thState, i_thZipcode, i_capacity, i_manUsername, ))

            cursor.callproc('admin_create_theater', (i_thName, i_comName, i_thStreet, i_thCity, i_thState, i_thZipcode, i_capacity, i_manUsername, ))
            
            connection.commit()

        connection.close()
        

    def CompanyDetail(self, filters):

        employees = self.admin_view_comDetail_emp(filters)
        theaters = self.admin_view_comDetail_th(filters)

        return {"ok":True, "employees":employees, "theaters":theaters}


    def admin_view_comDetail_emp(self, filters):
        i_comName = filters.get("i_comName")

        connection = get_conn()
        with connection.cursor() as cursor:
            
            print(i_comName)
            cursor.callproc('admin_view_comDetail_emp', (i_comName, ))
            data = cursor.fetchall()
            connection.commit()

        connection.close()
        return data

    
    def admin_view_comDetail_th(self, filters):
        i_comName = filters.get("i_comName")

        connection = get_conn()
        with connection.cursor() as cursor:
            
            print(i_comName)
            cursor.callproc('admin_view_comDetail_th', (i_comName, ))
            data = cursor.fetchall()
            connection.commit()

        connection.close()
        return data


    def CreateMovie(self, filters):

        i_movName = filters.get("movieName")
        i_movDuration = filters.get("duration")
        i_movReleaseDate = filters.get("releaseDate")



        connection = get_conn()
        with connection.cursor() as cursor:

            cursor.callproc('admin_create_mov', (i_movName, i_movDuration, i_movDuration, ))

        connection.close()
        
