from flask import Flask, jsonify, request


app = Flask(__name__)


items = [
    {'id': 1, 'name': 'item one', 'description': 'This is item one.'},
    {'id': 2, 'name': 'item two', 'description': 'This is item two.'}
]


@app.route('/')
def index():
    return 'Hello to our to do list!'

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return 'Item not found', 404

@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Bad request'}), 400

    new_id = items[-1]['id'] + 1 if items else 1
    item = {
        'id': new_id,
        'name': request.json.get('name'),
        'description': request.json.get('description','')
    }
    items.append(item)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Bad request'}), 400

    for item in items:
        if item['id'] == item_id:
            item['name'] = request.json.get('name')
            item['description'] = request.json.get('description','')
            return jsonify(item)
    return 'Item not found', 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            return 'Item deleted'
    return 'Item not found', 404



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')