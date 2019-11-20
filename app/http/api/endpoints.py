from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from ...util.custom_jwt import create_access_token
from ...services.LoginService import LoginService
from ...services.ManagerService import ManagerService

app = Flask(__name__)
CORS(app)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='trixie3008',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

# create services
login_service = LoginService(connection)
manager_service = ManagerService(connection)


@app.route('/userLogin', methods=['POST'])
def userLogin():
  data = request.get_json()
  user = data['user']
  try:
    success = login_service.login(user)
    if success:
      del user['password']

      access_token = create_access_token(identity=data)
      user['token'] = access_token
      return json_response({'ok': True, 'data': user})

  except Exception as e:
    print("Exception", e)

  return json_response({'message': 'Bad request parameters'}, 400)


@app.route('/TheaterOverview', methods=['GET'])
@login_required
def TheaterOverview():
  data = request.get_json()
  user = g.user
  manager_service.TheaterOverview


# #is this right? lol
# @app.route('/ScheduleMovie', methods=['GET'])
# @login_required
# def ScheduleMovie():
#   data=request.get_json()
#   user=g.user
#   manager_service.ScheduleMovie




#-------REGISTRATIONS--------
#user
@app.route('/userRegister', methods=['POST'])
def userRegister():
  data = request.get_json()
  user = data['user']
  try:
    with connection.cursor() as cursor:
      #Checking for duplicates
      sql = "SELECT `username`, `password` FROM `User`"
      cursor.execute(sql)
      userDatas = cursor.fetchall()
      for userData in userDatas:
        print(userData)
        if(user['Username'] == userData[0]):
          return({'message': 'Already an account with the username'}, 401)
      
      #Inserting the values to User
      sql = """INSERT INTO User (username,status,firstname,lastname,password)
                VALUES (%s,%s,%s,%s,%s)"""
      dataTuple = (user['Username'], 'Pending', user['firstName'], user['lastName'], user['password'])
      cursor.execute(sql, dataTuple)
      connection.commit()
      return json_response({'ok': True, 'data': user})
  except:
    print("Failed to insert record")
    return json_response({'message': 'Bad request parameters'}, 400)

#customer
@app.route('/customerRegister', methods=['POST'])
def customerRegister():
  data = request.get_json()
  user = data['user']
  try:
    with connection.cursor() as cursor:
      #Checking for duplicates in User
      sql = "SELECT `username`, `password` FROM `User`"
      cursor.execute(sql)
      userDatas = cursor.fetchall()
      for userData in userDatas:
        if(user['Username'] == userData[0]):
          return({'message': 'Already an account with the username'}, 401)

      #Checking for duplicates in CustomerCreditCards
      sql = "SELECT `creditCardNum` FROM `CustomerCreditCard`"
      cursor.execute(sql)
      cards = cursor.fetchall()
      customerCards = user['creditCardsList']
      for card in cards:
        card = int(card[0])
        for customerCard in customerCards:
          customerCard = int(customerCard)
          if(customerCard == card):
            print(customerCard)
            print(card)
            return({'message': 'Credit Card taken'}, 402)
      
      #Inserting the values to User
      sql = """INSERT INTO User (username,status,firstname,lastname,password)
                VALUES (%s,%s,%s,%s,%s)"""
      dataTuple = (user['Username'], 'Pending', user['firstName'], user['lastName'], user['password'])
      cursor.execute(sql, dataTuple)
      connection.commit()

      #Inserting the values to Customer
      sql = """INSERT INTO Customer (username)
                VALUES (%s)"""
      dataTuple = (user['Username'])
      cursor.execute(sql, dataTuple)
      connection.commit()

      #Inserting the values to CustomerCreditCard
      creditCards = user['creditCardsList']
      for creditCard in creditCards:
        sql = """INSERT INTO CustomerCreditCard (username, creditCardNum)
                  VALUES (%s, %s)"""
        dataTuple = (user['Username'], creditCard)
        cursor.execute(sql, dataTuple)
        connection.commit()
      return json_response({'ok': True, 'data': user})
  except pymysql.InternalError as e:
    print(e)
    print("Failed to insert record")
    return json_response({'message': 'Bad request parameters'}, 400)




@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  username = g.user
  return json_response({'response': param_1}, 200)


def json_response(payload, status_code=200):
   return json.dumps(payload), 200, {'Content-type': 'application/json'}
