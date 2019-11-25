import pymysql


def get_conn():
  connection = pymysql.connect(host='localhost',
                            user='root',
                            password='trixie3008',
                            db='moviez',
                            charset='utf8mb4',
                            port=3306,
                            cursorclass=pymysql.cursors.DictCursor)
  return connection

