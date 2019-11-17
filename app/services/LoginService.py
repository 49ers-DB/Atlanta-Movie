import pymysql.cursors

class LoginService(object):

  def __init__(self, connection):
    self.connection = connection


  def login(self, user) -> bool:
    with self.connection.cursor() as cursor:
      # Read a single record
      sql = "SELECT `username`, `password` FROM `User`"
      cursor.execute(sql)
      userDatas = cursor.fetchall()
      for userData in userDatas:
        if(user['username'] == userData[0]):
          if(user['password'] == userData[1]):
            return True
      
      return False