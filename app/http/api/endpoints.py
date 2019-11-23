from middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from app.util.custom_jwt import create_access_token
from app.services.LoginService import LoginService
from app.services.ManagerService import ManagerService
from app.services.RegisterService import RegisterService
from app.services.UserService import UserService


app = Flask(__name__)
CORS(app)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

# create services
login_service = LoginService(connection)
register_service = RegisterService(connection)
manager_service = ManagerService(connection)
user_service = UserService(connection)


#------------LOGIN------------
@app.route('/userLogin', methods=['POST'])
def userLogin():
  data = request.get_json()
  user = data['user']
  try:
    success = login_service.login(user)
    if success:
      del user['password']

      access_token = create_access_token(identity=data)
      user['jwt'] = access_token
      return json_response({'ok': True, 'data': user})

  except Exception as e:
    print("Exception", e)

  return json_response({'message': 'Bad request parameters'}, 400)



#-------REGISTRATIONS--------
#user
@app.route('/userRegister', methods=['POST'])
def userRegister():
  data = request.get_json()
  user = data['user']
  response = json_response({'message': 'Bad request parameters'}, 400)
  try:
    success = register_service.registerUser(user)
    print(success)
  
    if success:
      response = json_response({'ok': True, 'data': user})
    else: 
      response = json_response({'message': 'username taken'}, 401)
  except:
    response = json_response({'message': 'Bad request parameters'}, 400)
    print("Failed to insert record")

  return response
  

#customer
@app.route('/customerRegister', methods=['POST'])
def customerRegister():
  data = request.get_json()
  user = data
  try:
    response = register_service.registerCustomer(user)
    return json_response(response)
  except pymysql.InternalError as e:
    print(e)
    print("Failed to insert record")
  return json_response({'message': 'Bad request parameters'}, 400)


#manager
@app.route('/managerRegister', methods=['POST'])
def managerRegister():
  data = request.get_json()
  user = data
  try:
    response = register_service.registerManager(user)
    return json_response(response)
  except pymysql.InternalError as e:
    print(e)
    print("Failed to insert record")
  return json_response({'message': 'Bad request parameters'}, 400)

#managerCustomer
@app.route('/managerCustomerRegister', methods=['POST'])
def managerCustomerRegister():
  data = request.get_json()
  user = data
  try:
    response = register_service.registerManagerCustomer(user)
    return json_response(response)
  except pymysql.InternalError as e:
    print(e)
    print("Failed to insert record")
  return json_response({'message': 'Bad request parameters'}, 400)


#get the list of companies
@app.route('/getCompanies', methods=['GET'])
def getCompanies():
  response = manager_service.getCompanies()
  return json_response(response)
  

@app.route('/exploreTheater', methods=['GET'])
@login_required
def get_explore_theater():
  data = request.get_json()
  user = g.user
  print(data)
  #manager_service.TheaterOverview(user, data['filters'])

@app.route('/logVisit', methods=['POST'])
@login_required
def log_visit():
  data = request.get_json()
  user = g.user
  print(data)
  #manager_service.TheaterOverview(user, data['filters'])



@app.route('/TheaterOverview', methods=['GET'])
@login_required
def get_theater_overview():
  data = request.get_json()
  user = g.user
  manager_service.TheaterOverview(user, data['filters'])


# #is this right? lol
# @app.route('/ScheduleMovie', methods=['GET'])
# @login_required
# def ScheduleMovie():
#   data=request.get_json()
#   user=g.user
#   manager_service.ScheduleMovie





@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  user = g.user
  response = json_response({'userType': 'user'}, 200)
  userType = login_service.findUserType(user['username'])
  response = json_response({'userType': userType}, 200)


  return response
  

def json_response(payload, status_code=200):
   return json.dumps(payload), status_code, {'Content-type': 'application/json'}
