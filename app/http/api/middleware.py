from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions

import json

from app.util import custom_jwt


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    authorization = request.headers.get('authorization', None)
    if not authorization:
      return json.dumps({'error': 'no authorization token provided'}), 403, {'Content-type': 'application/json'}

    try:
      print(authorization)
      token = authorization.split(' ')[1]
      resp = decode(token, None, verify=False, algorithms=['HS256'])
      if custom_jwt.token_repo.get(resp['user']['username']) is None:
        print(custom_jwt.token_repo)
        return json.dumps({'error': 'wrong authorization token provided'}), 403, {'Content-type': 'application/json'}
      g.user = resp['user']

    except exceptions.DecodeError as e:
      print("Authorization Error:", e)
      return json.dumps({'error': 'DecodeTokenError'}), 403, {'Content-type': 'application/json'}

    return f(*args, **kwargs)

  return wrap
