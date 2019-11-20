

class RegisterService(object):

  def __init__(self, connection):
    self.connection = connection

  def registerUser(self, user) -> bool:
    username = user['username']
    firstname = user['firstname']
    lastname = user['lastname']
    password = user['password']

    with self.connection.cursor() as cursor:
      #Checking for duplicates

      sql = "SELECT `username` FROM `User` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      self.connection.commit()

      if len(userDatas) < 1:
        #Inserting the values to User
        sql = """INSERT INTO User (username, status, firstname, lastname, password)
                  VALUES (%s,%s,%s,%s,%s)"""
        dataTuple = (username, 'Pending', firstname, lastname, password)
        cursor.execute(sql, dataTuple)
        self.connection.commit()
        return True

      return False



  def registerCustomer(self, customer) -> bool:

    response = ({'message': 'Credit Card taken'}, 402)

    with self.connection.cursor() as cursor:
      credit_card_list = customer['creditCardsList']
      for i in range(5 - len(credit_card_list)):
        credit_card_list.append(None)

      credit_card_list = tuple(credit_card_list)

      sql = """SELECT count(`creditCardNum`) FROM `CustomerCreditCard` 
          where creditCardNum in (%s, %s, %s, %s, %s)"""
      cursor.execute(sql, credit_card_list)
      dup_count = cursor.fetchall()
      self.connection.commit()
      if dup_count > 0:
        return ({'message': 'Credit Card taken'}, 402)
      
      if self.registerUser(customer):

        #Inserting the values to Customer
        sql = """INSERT INTO Customer (username)
                  VALUES (%s)"""
        dataTuple = (customer['username'])
        cursor.execute(sql, dataTuple)
        self.connection.commit()

      #Inserting the values to CustomerCreditCard
      creditCards = customer['creditCardsList']
      for creditCard in creditCards:
        sql = """INSERT INTO CustomerCreditCard (username, creditCardNum) 
                  VALUES (%s, %s)"""
        dataTuple = (customer['username'], creditCard)
        cursor.execute(sql, dataTuple)
        self.connection.commit() 

      response = ({'ok': True, 'data': customer}, 200)

    return response