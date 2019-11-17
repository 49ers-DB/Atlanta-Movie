from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from ...util.custom_jwt import create_access_token
from ...services.LoginService import LoginService

app = Flask(__name__)
CORS(app)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306)

# create services
login_service = LoginService(connection)


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


@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  return json_response({'response': param_1}, 200)


def json_response(payload, status_code=200):
   return json.dumps(payload), 200, {'Content-type': 'application/json'}
