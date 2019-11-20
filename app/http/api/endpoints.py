from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from ...util.custom_jwt import create_access_token
from ...services.LoginService import LoginService
from ...services.ManagerService import ManagerService
from ...services.RegisterService import RegisterService

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
      user['token'] = access_token
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
    username = user['data']['username']
  
    if success:
      response = json_response({'ok': True, 'data': user})
    else: 
      response = json_response({'message': 'username: {} taken'.format(username)}, 402)
  except:
    response = json_response({'message': 'Bad request parameters'}, 400)
    print("Failed to insert record")

  return response
  

#customer
@app.route('/customerRegister', methods=['POST'])
def customerRegister():
  data = request.get_json()
  user = data['user']
  try:
    response = register_service.registerCustomer(user)
    return json_response(response)
  except pymysql.InternalError as e:
    print(e)
    print("Failed to insert record")
  return json_response({'message': 'Bad request parameters'}, 400)




@app.route('/TheaterOverview', methods=['GET'])
@login_required
def get_theater_overview():
  data = request.get_json()
  user = g.user
  manager_service.get_theater_overview_data(user, data['filters'])


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
  username = g.user
  return json_response({'response': param_1}, 200)


def json_response(payload, status_code=200):
   return json.dumps(payload), 200, {'Content-type': 'application/json'}
