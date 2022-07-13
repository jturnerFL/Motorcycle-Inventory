from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User, Bike, bike_schema, bikes_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/data')
def viewdata():
    return {'some': 'value'}

# CREATE Bike 
@api.route('/bikes', methods = ['POST'])
@token_required
def create_bike(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    max_speed = request.json['max_speed']
    weight = request.json['weight']
    cost_of_prod = request.json['cost_of_prod']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    bike = Bike(name,description,price, max_speed, weight,cost_of_prod,user_token = user_token )

    db.session.add(Bike)
    db.session.commit()

    response = bike_schema.dump(Bike)
    return jsonify(response)




# RETRIEVE ALL Bikes
@api.route('/bikes', methods = ['GET'])
@token_required
def get_bikes(current_user_token):
    owner = current_user_token.token
    bikes = Bike.query.filter_by(user_token = owner).all()
    response = bikes_schema.dump(Bike)
    return jsonify(response)


# RETRIEVE ONE Bike
@api.route('/bikes/<id>', methods = ['GET'])
@token_required
def get_bike(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        bike = Bike.query.get(id)
        response = bike_schema.dump(Bike)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401



# UPDATE Bike 
@api.route('/bikes/<id>', methods = ['POST','PUT'])
@token_required
def update_bike(current_user_token,id):
    bike = Bike.query.get(id) # GET Bike INSTANCE

    bike.name = request.json['name']
    bike.description = request.json['description']
    bike.price = request.json['price']
    bike.max_speed = request.json['max_speed']
    bike.weight = request.json['weight']
    bike.cost_of_prod = request.json['cost_of_prod']
    bike.user_token = current_user_token.token

    db.session.commit()
    response = bike_schema.dump(Bike)
    return jsonify(response)


# DELETE Bike
@api.route('/bikes/<id>', methods = ['DELETE'])
@token_required
def delete_bike(current_user_token, id):
    bike = bike.query.get(id)
    db.session.delete(Bike)
    db.session.commit()
    response = bike_schema.dump(Bike)
    return jsonify(response)