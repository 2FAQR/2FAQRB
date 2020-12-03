from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import QrDto
from ..service.qr_service import register, register_verify, login_verify, login, check_if_register

api = QrDto.api
_qr_login = QrDto.qr_login
_qr_register = QrDto.qr_register


@api.route('/login')
class QRLogin(Resource):
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        return login(auth_header)


@api.route('/register')
class QRRegister(Resource):
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        return register(auth_header)


@api.route('/verifylogin')
class QRLoginVerify(Resource):
    @api.expect(_qr_login, validate=True)
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        data = request.json
        return login_verify(data, auth_header)


@api.route('/verifyregister')
class QRRegisterVerify(Resource):
    @api.expect(_qr_register, validate=True)
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        data = request.json
        return register_verify(data, auth_header)

@api.route('/checkifregister')
class CheckIfRegister(Resource):
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        return check_if_register(auth_header)



