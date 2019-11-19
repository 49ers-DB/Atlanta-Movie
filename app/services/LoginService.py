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