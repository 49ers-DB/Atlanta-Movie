import pymysql.cursors

class LoginService(object):

  def __init__(self, connection):
    self.connection = connection


  def login(self, user) -> bool:

    with self.connection.cursor() as cursor:
      # Read a single record
      sql = "SELECT `username`, `password` FROM `User` where username=(%s) and password=(%s)"
      cursor.execute(sql, (user['username'], user['password']))
      userDatas = cursor.fetchall()
      self.connection.commit()

      if len(userDatas) > 0:
        return True
      
      return False

  def findUserType(self, username):
    manager = False
    admin = False
    customer = False
    
    with self.connection.cursor() as cursor:
      #Check Manager
      sql = "SELECT `username` FROM `Manager` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      self.connection.commit()
      if len(userDatas) > 0:
        manager = True
      
      #Check Cutomer
      sql = "SELECT `username` FROM `Customer` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      self.connection.commit()
      if len(userDatas) > 0:
        customer = True
      
      #Check Admin
      sql = "SELECT `username` FROM `Admin` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      self.connection.commit()
      if len(userDatas) > 0:
        admin = True
    
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