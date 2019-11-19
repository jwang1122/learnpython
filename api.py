from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return{
            'product': ['Ice cream',
            'Chocolate', 'Fruit']
        }

api.add_response(Product, '/')

if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)