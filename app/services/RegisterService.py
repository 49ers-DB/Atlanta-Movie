

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
      if dup_count[0].get(('count(`creditCardNum`)')) > 0:
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
          if(creditCard != None):
            sql = """INSERT INTO CustomerCreditCard (username, creditCardNum) 
                      VALUES (%s, %s)"""
            dataTuple = (customer['username'], creditCard)
            cursor.execute(sql, dataTuple)
            self.connection.commit() 

      response = ({'ok': True, 'data': customer}, 200)

    return response

  def registerManager(self, manager) -> bool:
    with self.connection.cursor() as cursor:
      if self.registerUser(manager):
        address = (manager['address'], manager['city'], manager['selectedState']['value'], manager['zipCode'])
        print(address)
        sql = "SELECT `username` FROM `Manager` WHERE manStreet=(%s) AND manCity=(%s) AND manState=(%s) AND manZipCode=(%s)"
        cursor.execute(sql, address)
        userDatas = cursor.fetchall()
        self.connection.commit()
        print(userDatas)
        if len(userDatas) < 1:
          #Inserting the values to Employee
          sql = """INSERT INTO Employee (username)
                    VALUES (%s)"""
          dataTuple = (manager['username'])
          cursor.execute(sql, dataTuple)
          self.connection.commit()

          #Inserting the values to Manager
          sql = """INSERT INTO Manager (username, manStreet, manCity, manState, manZipCode, comName)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
          dataTuple = (manager['username'], manager['address'], manager['city'], manager['selectedState']['value'], manager['zipCode'], manager['selectedCompany']['value'])
          cursor.execute(sql, dataTuple)
          self.connection.commit()

          response = ({'ok': True, 'data': manager}, 200)
        else:
          print("here")
          response = ({'Address already taken': False, 'data': manager}, 402)

    return response
  def registerManagerCustomer(self, managerCustomer) -> bool:
    print(managerCustomer)
    with self.connection.cursor() as cursor:
      if(self.registerCustomer(managerCustomer)):
        address = (managerCustomer['address'], managerCustomer['city'], managerCustomer['selectedState']['value'], managerCustomer['zipCode'])
        print(address)
        sql = "SELECT `username` FROM `Manager` WHERE manStreet=(%s) AND manCity=(%s) AND manState=(%s) AND manZipCode=(%s)"
        cursor.execute(sql, address)
        userDatas = cursor.fetchall()
        self.connection.commit()
        print(userDatas)
        if len(userDatas) < 1:
          #Inserting the values to Employee
          sql = """INSERT INTO Employee (username)
                    VALUES (%s)"""
          dataTuple = (managerCustomer['username'])
          cursor.execute(sql, dataTuple)
          self.connection.commit()

          #Inserting the values to Manager
          sql = """INSERT INTO Manager (username, manStreet, manCity, manState, manZipCode, comName)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
          dataTuple = (managerCustomer['username'], managerCustomer['address'], managerCustomer['city'], managerCustomer['selectedState']['value'], managerCustomer['zipCode'], managerCustomer['selectedCompany']['value'])
          cursor.execute(sql, dataTuple)
          self.connection.commit()

          response = ({'ok': True, 'data': managerCustomer}, 200)
        else:
          print("here")
          response = ({'Address already taken': False, 'data': managerCustomer}, 403)

        

      return response

