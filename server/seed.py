from flask import Blueprint, jsonify, request
from .models import db, Plant

api = Blueprint('api', __name__)

@api.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.serialize() for plant in plants])

@api.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.serialize())

@api.route('/plants', methods=['POST'])
def create_plant():
    data = request.json
    new_plant = Plant(name=data['name'], image=data['image'], price=data['price'])
    db.session.add(new_plant)
    db.session.commit()