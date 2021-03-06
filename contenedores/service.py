from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({'status': 'ok'})

class Status(Resource):
    def get(self):
        return jsonify({'status': 'ok'})


api.add_resource(Home, '/')
api.add_resource(Status, '/status')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
