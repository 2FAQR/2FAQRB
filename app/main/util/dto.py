from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class QrDto:
    api = Namespace('qrcode', description='qr code related operations')
    qr_register = api.model('qr_register', {
        'hash': fields.String(required=True, description='The hash'),
        'public_key': fields.String(required=True, description='The public key needed to be stored')
    })
    qr_login = api.model('qr_login', {
        'hash': fields.String(required=True, description='The orginal hash')
    })