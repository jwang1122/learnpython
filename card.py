import os
import uuid
import stripe

from flask import Flask, request

card = Flask(__name__)
card.config.from_object(__name__)

@card.route('/hello', methods=['GET'])
def hello():
    return '<h3>Hello, the World!</h3>'

if __name__ == '__main__':
    card.run()