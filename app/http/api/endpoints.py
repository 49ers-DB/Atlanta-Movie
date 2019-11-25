from middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from app.util.custom_jwt import create_access_token
from app.services.LoginService import LoginService
from app.services.ManagerService import ManagerService
from app.services.RegisterService import RegisterService
from app.services.DropDownService import DropDownService
from app.services.UserService import UserService
from app.services.CustomerService import CustomerService


app = Flask(__name__)
CORS(app)


# create services
login_service = LoginService()
register_service = RegisterService()
manager_service = ManagerService()
drop_down_service = DropDownService()
user_service = UserService()
customer_service = CustomerService()


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


#-------DropDownService---------
@app.route('/getCompanies', methods=['GET'])
def getCompanies():
  response = drop_down_service.CompanyDropDown()
  return json_response(response)

@app.route('/movies', methods=['GET'])
def getMovies():
  response = drop_down_service.MovieDropDown()
  return json_response(response)

@app.route('/theaters/<string:comName>', methods=['GET'])
@login_required
def getTheaters(comName):

  theaters = drop_down_service.TheaterDropDown(comName)
  return json_response({'ok': True, 'theaters': theaters})

@app.route('/creditcard', methods=['GET'])
@login_required
def getCreditCardNumbers():
  username = g.user['username']

  response = drop_down_service.getCreditCardNumbers(username)
  return json_response(response)
  

#----------UserService--------------------
@app.route('/exploreTheater', methods=['POST'])
@login_required
def explore_theater():
  data = request.get_json()
  print(data)  
  query_data = user_service.ExploreTheater(data)
  return json_response({'ok': True, 'theaters': query_data})

@app.route('/logVisit', methods=['POST'])
@login_required
def log_visit():
  data = request.get_json()
  user = g.user['username']

  user_service.LogVisit(user, data)
  return json_response({'ok': True})


#--------CustomerService-------------------
@app.route('/exploreMovie', methods=['POST'])
@login_required
def explore_movie():
  data = request.get_json()
  
  query_data = customer_service.ExploreMovie(data)
  return json_response({'ok': True, 'moviePlays': query_data})


@app.route('/viewMovie', methods=['POST'])
@login_required
def view_movie():
  data = request.get_json()
  username = g.user['username']
  
  customer_service.ViewMovie(username, data)
  return json_response({'ok': True})



#----------ManagerService-----------------
@app.route('/TheaterOverview', methods=['POST'])
@login_required
def get_theater_overview():
  data = request.get_json()
  user = g.user
  response = manager_service.TheaterOverview(user, data)

  return json_response({'ok': True, 'info': response})


@app.route('/moviePlay', methods=['POST'])
@login_required
def ScheduleMovie():
  data=request.get_json()
  user=g.user['username']

  manager_service.ScheduleMovie(user, data)

  return json_response({'ok': True})





@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  user = g.user
  # response = json_response({'userType': 'user'}, 200)
  # userType = login_service.findUserType(user['username'])
  # response = json_response({'userType': userType}, 200)


  return json_response({'ok':True})

@app.route("/user", methods=['GET'])
@login_required
def get_user_type():
  user = g.user
  response = json_response({'userType': 'user'}, 200)
  userType = login_service.findUserType(user['username'])
  response = json_response({'userType': userType}, 200)

  return response
  

def json_response(payload, status_code=200):
   return json.dumps(payload), status_code, {'Content-type': 'application/json'}



#----------CustomerService--------------------
@app.route('/viewHistory', methods=['POST'])
@login_required
def viewHistory():
  user = g.user['username']
  print(user)

  data = customer_service.ViewHistory(user)
  return json_response({'data': data})