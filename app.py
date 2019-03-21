
from flask import Flask, jsonify

# special python variable __name__ gives each file a unique name
app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# decorator
# end point, request that it's going to understand

# ! '@app.route' by default is a GET request


@app.route('/')  # 'http://www.google.com/'
def home():
    return "Hello World!"

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    return jsonify({item: stores['item']['name']})


app.run(port=5000)
