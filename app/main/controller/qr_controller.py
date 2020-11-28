from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import QrDto
from ..service.qr_service import register, register_verify, login_verify, login

api = QrDto.api
_qr_login = QrDto.qr_login
_qr_register = QrDto.qr_register


@api.route('/login')
class QRLogin(Resource):
    @api.expect(_qr_login, validate=True)
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        data = request.json
        return login(data, auth_header)


@api.route('/register')
class QRRegister(Resource):
   @api.expect(_qr_login, validate=True)
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        data = request.json
        return register(data, auth_header)


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
   @api.expect(_qr_login, validate=True)
    def post(self):
        """Creates a new User """
        auth_header = request.headers.get('Authorization')
        data = request.json
        return register_verify(data, auth_header)



