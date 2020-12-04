from app.main.model.user import User
import os
import datetime
from base64 import b64encode
from app.main import db
from ecies import encrypt, decrypt
from ecies.utils import generate_eth_key, generate_key
import binascii


auth_time = 1000000000
max_try = 3

def getHash():
  return b64encode(os.urandom(16)).decode('utf-8')

def token_to_user(auth_header):
  if not auth_header:
    return None
  token = auth_header.split(" ")[1]
  user_id = User.decode_auth_token(token)
  user = User.query.get(user_id)
  return user

def register(auth_header):
  '''
    Check for the jwt token received with the header and retrieve the user.
    Create a new hash in the user model.
    send the hash in return with 200 status code.
  '''
  user = token_to_user(auth_header)
  if not user:
    return {
      'message': 'User not found. Please check the user.'
    }, 401
  hash = getHash()
  user.hash = hash
  user.hash_verified = datetime.datetime.now()
  user.can_verify = max_try+1
  save_changes(user)
  return {
    'hash': user.hash
  }, 200

def register_verify(data, auth_header):
  '''
    Get the user from jwt token.
    Verify the hash received with the request.
    update the public key received with the request.
  '''
  hash = data.get('hash')
  public_key = data.get('public_key')
  user = token_to_user(auth_header)
  if user == None:
    return {
      "message": "Cannot find user"
    }, 401
  if user.hash != hash:
    return {
      "message": "Hash not verified"
    }, 401
  user.public_key = public_key
  user.can_verify = 0
  user.hash_verified = datetime.datetime.now()
  save_changes(user)
  return {
    'message': 'pkey updated successfully'
  }, 200


def login_verify(data, auth_header):
  '''
    Get the user from jwt token.
    get the hash received and check with the hash created for this.

  '''
  hash = data.get('hash')
  user = token_to_user(auth_header)
  # data = decrypt(user.public_key, hash)

  user.can_verify = 0
  user.hash_verified = datetime.datetime.now()
  save_changes(user)
  if hash == user.hash:
    return {
      "message": "Success verification"
    }, 200
  return {
    "message": "hash cannot be verified"
  }, 401

def login(auth_header):
  '''
    Check the JWT token received with the request.
    Create a hash and encrypt with the public key and send to the frontend
  '''
  user = token_to_user(auth_header)
  if not user:
    return {
      'message': 'User not found. Please check the user.'
    }, 401
  random_string = getHash()
  print(user.public_key)
  random_string_hash = binascii.b2a_hex(encrypt(user.public_key, bytes(random_string, 'utf-8'))).decode('utf-8')
  print(random_string_hash)
  user.hash = random_string
  user.can_verify = max_try+1
  save_changes(user)
  return {
    'hash': random_string_hash
  }, 200


def check_if_register(auth_header):
  user = token_to_user(auth_header)
  if not user:
    return {
      'message': 'User not found.'
    }, 401
  if user.can_verify > max_try:
    return {
      'message': "Maximum try occured"
    }, 402
  user.can_verify = user.can_verify + 1
  save_changes(user)
  if (datetime.datetime.now() - user.hash_verified).total_seconds() >= auth_time:
    return {
      'message': 'Max time has passed'
    }, 401
  return {
    'message': 'Just verified'
  }, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

