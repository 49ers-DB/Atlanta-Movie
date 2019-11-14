from jwt import encode
from json import JSONEncoder
import secrets

private_key = secrets.token_urlsafe(128)
token_repo = dict()

def create_access_token(identity):
  token = encode(identity, private_key).decode('utf-8')
  username = identity['user']['username']
  token_repo[username] = token
  return token
