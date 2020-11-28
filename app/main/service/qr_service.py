from app.main.model.qr import UserHash
from app.main.model.user import User

def register(data, auth_header):
  '''
    Check for the jwt token received with the header and retrieve the user.
    Create a new hash in the user model.
    send the hash in return with 200 status code.
  '''
  pass

def register_verify(data, auth_header):
  '''
    Get the user from jwt token.
    Verify the hash received with the request.
    update the public key received with the request.
  '''
  pass

def login_verify(data, auth_header):
  '''
    Get the user from jwt token.
    get the hash received and check with the hash created for this.

  '''
  pass

def login(data, auth_header):
  '''
    Check the JWT token received with the request.
    Create a hash and encrypt with the public key and send to the frontend
  '''
  pass