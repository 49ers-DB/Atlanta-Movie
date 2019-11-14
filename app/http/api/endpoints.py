from .middleware import login_required
from flask import Flask, json, g, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/example/<int:param_1>", methods=['GET'])
@login_required
def example_endpoint(param_1):
  print(param_1)
  return json_response({'response', param_1}, 200)

def json_response(payload, status_code=200):
   return json.dumps(payload), 200, {'Content-type': 'application/json'}
