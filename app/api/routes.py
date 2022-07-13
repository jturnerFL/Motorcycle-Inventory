from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User, bike

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/data')
def viewdata():
    return {'some': 'value'}

