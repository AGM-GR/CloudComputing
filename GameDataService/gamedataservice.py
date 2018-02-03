import pymongo
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from json import loads
from bson.json_util import dumps
from bson import ObjectId

app = Flask(__name__)
api = Api(app)
CORS(app)

# Connect with the Mongo data base
try:
    conn = pymongo.MongoClient('mongoservice:27017')
    resultconexion = "Connected successfully"
except pymongo.errors.ConnectionFailure as error:
    resultconexion = "Could not connect to MongoDB: %s" % error

print (resultconexion)

gamesdb = conn.gamedata


# Data groups for requests
gameParser = reqparse.RequestParser()
gameParser.add_argument('name')
gameParser.add_argument('platform')

playerParser = reqparse.RequestParser()
playerParser.add_argument('name')
playerParser.add_argument('score')
playerParser.add_argument('location')


# API REST Functions

class Home(Resource):
    def get(self):
        return jsonify({'service_name': 'GameData', 'service_version': '1.0'})

class Status(Resource):
    def get(self):
        return jsonify({'status': 'ok'})

class GamesList(Resource):
    def get(self):
        result = gamesdb.games.find()
        return loads(dumps(result))

class GameData(Resource):
    def get(self, game_id):
        result = gamesdb.games.find({"_id": ObjectId(game_id)})[0]
        return loads(dumps(result))

    def put(self, game_id):
        args = gameParser.parse_args()
        game_name = args['name']
        game_platform = args['platform']

        result = gamesdb.games.update_one({"_id": ObjectId(game_id)}, {"$set": {"name": game_name, "platform": game_platform}}, upsert=False)
        return jsonify({"updated": result.modified_count})

    def delete(self, game_id):
        result = gamesdb.games.delete_many({"_id": ObjectId(game_id)})
        resultplayers = gamesdb.players.delete_many({"gameId": game_id})
        return jsonify({"deleted": result.deleted_count, "deleted_players": resultplayers.deleted_count})

class GameInsert(Resource):
    def post(self):
        args = gameParser.parse_args()
        game_name = args['name']
        game_platform = args['platform']

        result = gamesdb.games.insert({"name": game_name, "platform": game_platform})
        return loads(dumps(result))

class GamePlayersList(Resource):
    def get(self, game_id):
        result = gamesdb.players.find({"gameId": game_id})
        return loads(dumps(result))

class GamePlayerData(Resource):
    def get(self, game_id, player_id):
        result = gamesdb.players.find({"_id": ObjectId(player_id)})[0]
        return loads(dumps(result))

    def put(self, game_id, player_id):
        args = playerParser.parse_args()
        player_name = args['name']
        player_score = args['score']
        player_location = args['location']

        result = gamesdb.players.update_one({"_id": ObjectId(player_id)}, {"$set": {"gameId": game_id, "playerName": player_name, "playerScore": player_score, "playerLocation": player_location}}, upsert=False)
        return jsonify({"updated": result.modified_count})

    def delete(self, game_id, player_id):
        result = gamesdb.players.delete_many({"_id": ObjectId(player_id)})
        return jsonify({"deleted": result.deleted_count})

class GamePlayerInsert(Resource):
    def post(self, game_id):
        args = playerParser.parse_args()
        player_name = args['name']
        player_score = args['score']
        player_location = args['location']

        result = gamesdb.players.insert({"gameId": game_id, "playerName": player_name, "playerScore": player_score, "playerLocation": player_location})
        return loads(dumps(result))

#API REST addresses
api.add_resource(Home, '/')
api.add_resource(Status, '/status')
api.add_resource(GamesList, '/games')
api.add_resource(GameData, '/game/<game_id>')
api.add_resource(GameInsert, '/game')
api.add_resource(GamePlayersList, '/game/<game_id>/players')
api.add_resource(GamePlayerData, '/game/<game_id>/player/<player_id>')
api.add_resource(GamePlayerInsert, '/game/<game_id>/player')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
