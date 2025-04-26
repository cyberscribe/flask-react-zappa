from flask import Blueprint, jsonify, request
from includes.models import Item, db_session

api_bp = Blueprint('api', __name__, url_prefix='/api/')

@api_bp.route('/item/', methods=['GET'])
def get_items():
    items = db_session.query(Item).all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])

@api_bp.route('/item/', methods=['POST'])
def create_item():
    data = request.json
    item = Item(name=data.get('name', ''))
    db_session.add(item)
    db_session.commit()
    return jsonify({"message": "Item created", "item": {"id": item.id, "name": item.name}})

@api_bp.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = db_session.query(Item).filter_by(id=item_id).first()
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.json
    item.name = data.get('name', item.name)
    db_session.commit()
    return jsonify({"message": "Item updated", "item": {"id": item.id, "name": item.name}})

@api_bp.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = db_session.query(Item).filter_by(id=item_id).first()
    if not item:
        return jsonify({"error": "Item not found"}), 404
    db_session.delete(item)
    db_session.commit()
    return jsonify({"message": "Item deleted"})
