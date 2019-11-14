from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
from ...util.custom_jwt import create_access_token

app = Flask(__name__)
CORS(app)

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
