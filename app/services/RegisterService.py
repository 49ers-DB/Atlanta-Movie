from app.services.DBService import get_conn


class RegisterService(object):

  def registerUser(self, user):
    username = user['username']
    firstname = user['firstname']
    lastname = user['lastname']
    password = user['password']

    connection = get_conn()
    with connection.cursor() as cursor:

      cursor.callproc("user_register", (username, password, firstname, lastname, ))
      connection.commit()

    connection.close()
  
  def registerCustomer(self, customer) -> bool:

    response = ({'message': 'Credit Card taken'}, 402)
    username = customer['username']
    firstname = customer['firstname']
    lastname = customer['lastname']
    password = customer['password']

    connection = get_conn()
    with connection.cursor() as cursor:

      cursor.callproc("customer_only_register", (username, password, firstname, lastname, ))
      connection.commit()

      credit_card_list = customer['creditCardsList']
      try:
        for credit_card_num in credit_card_list:
          cursor.callproc("customer_add_creditcard", (username, credit_card_num,))
          print(cursor.fetchall())
          connection.commit()

      except:
        return response

    connection.close()
    return ({'ok': True, 'data': customer}, 200)



  def registerManager(self, manager):
    i_username = manager.get("username")
    i_password = manager.get('password')
    i_firstname = manager.get('firstname')
    i_lastname = manager.get('lastname')
    #TODO fix the comname and state with the register selects
    i_comName = manager['selectedCompany']['value']
    i_empStreet = manager.get('address')
    i_empCity = manager.get('city')
    i_empState = manager['selectedState']['value']
    i_empZipcode = manager['zipCode']

    connection = get_conn()
    with connection.cursor() as cursor:

      cursor.callproc("manager_only_register", (i_username, i_password, i_firstname, i_lastname, i_comName, i_empStreet, i_empCity, i_empState, i_empZipcode, ))
    connection.commit()
    connection.close()

  def registerManagerCustomer(self, managerCustomer) -> bool:
    response = ({'message': 'Credit Card taken'}, 402)
    i_username = managerCustomer.get("username")
    i_password = managerCustomer.get('password')
    i_firstname = managerCustomer.get('firstname')
    i_lastname = managerCustomer.get('lastname')
    #TODO fix the comname and state with the register selects
    i_comName = managerCustomer['selectedCompany']['value']
    i_empStreet = managerCustomer.get('address')
    i_empCity = managerCustomer.get('city')
    i_empState = managerCustomer['selectedState']['value']
    i_empZipcode = managerCustomer['zipCode']
    
    connection = get_conn()
    with connection.cursor() as cursor:
      cursor.callproc("manager_customer_register", (i_username, i_password, i_firstname, i_lastname, i_comName, i_empStreet, i_empCity, i_empState, i_empZipcode, ))
      connection.commit()
    
      credit_card_list = managerCustomer['creditCardsList']
      try:
        for credit_card_num in credit_card_list:
          cursor.callproc("customer_add_creditcard", (i_username, credit_card_num,))
          connection.commit()

      except:
        return response

    connection.close()
    return ({'ok': True, 'data': managerCustomer}, 200)

  

  def registerUser1(self, user) -> bool:
    username = user['username']
    firstname = user['firstname']
    lastname = user['lastname']
    password = user['password']

    connection = get_conn()
    with connection.cursor() as cursor:
      #Checking for duplicates

      sql = "SELECT `username` FROM `User` where username=(%s)"
      cursor.execute(sql, (username))
      userDatas = cursor.fetchall()
      connection.commit()

      success = False

      if len(userDatas) < 1:
        #Inserting the values to User
        sql = """INSERT INTO User (username, status, firstname, lastname, password)
                  VALUES (%s,%s,%s,%s,MD5(%s))"""
        dataTuple = (username, 'Pending', firstname, lastname, password)
        cursor.execute(sql, dataTuple)
        connection.commit()

        success = True

      connection.close()
      return success



  def registerCustomer1(self, customer) -> bool:

    response = ({'message': 'Credit Card taken'}, 402)

    connection = get_conn()

    with connection.cursor() as cursor:

      
      credit_card_list = customer['creditCardsList']
      for i in range(5 - len(credit_card_list)):
        credit_card_list.append(None)

      credit_card_list = tuple(credit_card_list)

      sql = """SELECT count(`creditCardNum`) FROM `CustomerCreditCard` 
          where creditCardNum in (%s, %s, %s, %s, %s)"""
      cursor.execute(sql, credit_card_list)
      dup_count = cursor.fetchall()
      connection.commit()
      if dup_count[0].get(('count(`creditCardNum`)')) > 0:
        return ({'message': 'Credit Card taken'}, 402)
      
      if self.registerUser(customer):

        #Inserting the values to Customer
        sql = """INSERT INTO Customer (username)
                  VALUES (%s)"""
        dataTuple = (customer['username'])
        cursor.execute(sql, dataTuple)
        connection.commit()

        #Inserting the values to CustomerCreditCard
        creditCards = customer['creditCardsList']
        for creditCard in creditCards:
          if(creditCard != None):
            sql = """INSERT INTO CustomerCreditCard (username, creditCardNum) 
                      VALUES (%s, %s)"""
            dataTuple = (customer['username'], creditCard)
            cursor.execute(sql, dataTuple)
            connection.commit() 

      connection.close()
      response = ({'ok': True, 'data': customer}, 200)

    return response

  

  def registerManager1(self, manager) -> bool:

    connection = get_conn()
    with connection.cursor() as cursor:

      address = (manager['address'], manager['city'], manager['selectedState']['value'], manager['zipCode'])
      
      sql = "SELECT `username` FROM `Manager` WHERE manStreet=(%s) AND manCity=(%s) AND manState=(%s) AND manZipCode=(%s)"
      cursor.execute(sql, address)
      userDatas = cursor.fetchall()
      connection.commit()

      if len(userDatas) < 1 and self.registerUser(manager):

        #Inserting the values to Employee
        sql = """INSERT INTO Employee (username)
                  VALUES (%s)"""
        dataTuple = (manager['username'])
        cursor.execute(sql, dataTuple)
        connection.commit()

        #Inserting the values to Manager
        sql = """INSERT INTO Manager (username, manStreet, manCity, manState, manZipCode, comName)
                  VALUES (%s, %s, %s, %s, %s, %s)"""
        dataTuple = (manager['username'], manager['address'], manager['city'], manager['selectedState']['value'], manager['zipCode'], manager['selectedCompany']['value'])
        cursor.execute(sql, dataTuple)
        connection.commit()

        response = ({'ok': True, 'data': manager}, 200)
      else:

        response = ({'Address already taken': False, 'data': manager}, 402)
    connection.close()
    return response


  def registerManagerCustomer1(self, managerCustomer) -> bool:
    
    connection = get_conn()

    with connection.cursor() as cursor:

      address = (managerCustomer['address'], managerCustomer['city'], managerCustomer['selectedState']['value'], managerCustomer['zipCode'])
      sql = "SELECT `username` FROM `Manager` WHERE manStreet=(%s) AND manCity=(%s) AND manState=(%s) AND manZipCode=(%s)"
      cursor.execute(sql, address)
      userDatas = cursor.fetchall()
      connection.commit()

      if len(userDatas) < 1 and self.registerCustomer(managerCustomer)[0]['ok']:

        #Inserting the values to Employee
        sql = """INSERT INTO Employee (username)
                  VALUES (%s)"""
        dataTuple = (managerCustomer['username'])
        cursor.execute(sql, dataTuple)
        connection.commit()

        #Inserting the values to Manager
        sql = """INSERT INTO Manager (username, manStreet, manCity, manState, manZipCode, comName)
                  VALUES (%s, %s, %s, %s, %s, %s)"""
        dataTuple = (managerCustomer['username'], managerCustomer['address'], managerCustomer['city'], managerCustomer['selectedState']['value'], managerCustomer['zipCode'], managerCustomer['selectedCompany']['value'])
        cursor.execute(sql, dataTuple)
        connection.commit()

        response = ({'ok': True, 'data': managerCustomer}, 200)
      else:
        print("here")
        response = ({'Address already taken': False, 'data': managerCustomer}, 403)
        
      connection.close()
      
      return response

