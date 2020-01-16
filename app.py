import os

from flask import Flask, request, make_response, jsonify
from  sqlalchemy.sql.expression import func

from models.base import db
from models.cards import Card
# Init Flask
app = Flask(__name__)


basedir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
# Init db
db.init_app(app)

##### ROUTERS #####

@app.route("/get_random")
def get_random():
    res = Card.query.order_by(func.random()).limit(1)
    return {'back_side': res[0].back_side, 'front_side': res[0].front_side}


@app.route("/card/<id>")
def get_card(id):
    c = Card.query.get(id)
    return {'back_side': c.back_side, 'front_side': c.front_side}


@app.route("/card", methods=['POST'])
def post_card():
    fs = request.json['fron_side']
    bs = request.json['back_side']

    c = Card(front_side=fs, back_side=bs)
    db.session.add(c)
    try:
        db.session.commit()
    except Exception as exc:
        data = {'message': str(exc), 'code': 'Fail'}
        return make_response(jsonify(data), 500)
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


@app.route("/card/<id>", methods=['PUT'])
def update_card(id):
    c = Card.query.get(id)
    if not c:
        data = {'message': 'Not Found', 'code': 'Fail'}
        return make_response(jsonify(data), 404)
    fs = request.json['front_side']
    bs = request.json['back_side']

    c.front_side=fs
    c.back_side=bs
    try:
        db.session.commit()
    except Exception as exc:
        data = {'message': str(exc), 'code': 'Fail'}
        return make_response(jsonify(data), 500)
    data = {'message': 'Updated', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)

# DEBUG
if __name__ == "__main__":
    app.run(debug=True)
