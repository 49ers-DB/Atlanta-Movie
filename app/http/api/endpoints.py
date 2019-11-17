from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
import pymysql.cursors
from ...util.custom_jwt import create_access_token

app = Flask(__name__)
CORS(app)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306)


@app.route('/userLogin', methods=['POST'])
def userLogin():
  data = request.get_json()
  user = data['user']
  try:
    with connection.cursor() as cursor:
      # Read a single record
      sql = "SELECT `username`, `password` FROM `User`"
      cursor.execute(sql)
      userDatas = cursor.fetchall()
      for userData in userDatas:
        if(user['username'] == userData[0]):
          if(user['password'] == userData[1]):
            del user['password']
            access_token = create_access_token(identity=data)
            user['token'] = access_token
            return json_response({'ok': True, 'data': user})
  except Exception as e:
    print("Exception", e)
    return json_response({'message': 'Bad request parameters'}, 400)

      # print(result)



@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  return json_response({'response': param_1}, 200)
  
@app.route("/auth", methods=['POST'])
def auth_user():
  data = request.get_json()
  user = data['user']
  try:
    if user['username'] == 'ed':
      # todo call LoginService to get the user
      del user['password']
      access_token = create_access_token(identity=data)
      user['token'] = access_token
      return json_response({'ok': True, 'data': user})
  except Exception as e:
    print("Exception", e)
    return json_response({'message': 'Bad request parameters'}, 400)



def json_response(payload, status_code=200):
   return json.dumps(payload), 200, {'Content-type': 'application/json'}
