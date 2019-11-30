import pymysql.cursors
from app.services.DBService import get_conn

class LoginService(object):


  def login(self, user) -> bool:

    connection = get_conn()

    with connection.cursor() as cursor:
      # Read a single record
      sql = "SELECT `username`, `password`, status FROM `User` where username=(%s) and password=MD5(%s)"
      cursor.execute(sql, (user['username'], user['password']))
      userDatas = cursor.fetchall()
      connection.commit()
      connection.close()
    
      if len(userDatas) == 1 and userDatas[0]['status']!='Declined':
        return True
      
      return False

      

  def findUserType(self, username):
    manager = False
    admin = False
    customer = False
    connection = get_conn()
    
    with connection.cursor() as cursor:
      #Check Manager
      sql = "SELECT `username` FROM `Manager` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      connection.commit()
      if len(userDatas) > 0:
        manager = True
      
      #Check Cutomer
      sql = "SELECT `username` FROM `Customer` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      connection.commit()
      if len(userDatas) > 0:
        customer = True
      
      #Check Admin
      sql = "SELECT `username` FROM `Admin` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      connection.commit()
      if len(userDatas) > 0:
        admin = True

    connection.close()
    
    userType = 'user'
    if(manager):
      userType = 'manager'
      if(customer):
        userType = 'manager-customer'
        return userType
    elif(admin):
      userType = 'admin'
      if(customer):
        userType = 'admin-customer'
        return userType
    elif(customer):
      userType = 'customer'
    return userType