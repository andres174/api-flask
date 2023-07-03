from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json


app = Flask(__name__)
api = Api(app)

#/users
users_path = './data/users.csv'
users_json = './data/users.json'
#/locations
locs_path = './data/locations.csv'
locs_json = './data/locations.json'

class Users(Resource):
    def get(self):
        # data = pd.read_csv(users_path)
        # #data = data.to_dict()
        # data.to_json(users_json)
        # d = open(users_json)
        # return jsonify(d), 200
        
        data =  {
                0: {
                    "userId": "a1b",
                    "name": "Joe",
                    "city": "Paris"
                },
                1: {
                    "userId": "a2c",
                    "name": "Jenny",
                    "city": "London"
                },
                2: {
                    "userId": "b1b",
                    "name": "Jack",
                    "city": "London"
                },
                3: {
                    "userId": "b2c",
                    "name": "Jill",
                    "city": "Berlin"
                }
            }
        return data
    


class Locations(Resource):
    def get(self):
        # data = pd.read_csv(locs_path)
        # data.to_json(locs_json)
        # return {'data': data}, 200
        data = {
                0: {
                    "locationId": "1",
                    "name": "Cafe de Flore",
                    "rating": 4.0
                },
                1: {
                    "locationId": "2",
                    "name": "Cafe Tabac",
                    "rating": 4.6
                },
                2: {
                    "locationId": "3",
                    "name": "Rosslyn Coffee",
                    "rating": 4.8
                },
                3: {
                    "locationId": "4",
                    "name": "Three Wheels Coffee",
                    "rating": 4.6
                },
                4: {
                    "locationId": "5",
                    "name": "Roasting Plant Coffee",
                    "rating": 4.4
                },
                5: {
                    "locationId": "6",
                    "name": "Distrikt coffee",
                    "rating": 4.4
                },
                6: {
                    "locationId": "7",
                    "name": "Westberlin",
                    "rating": 4.4
                }
            }
        return data, 200

#api.com/users
api.add_resource(Users, '/users')
#api.com/locations
api.add_resource(Locations, '/locations')

if __name__ == "__main__":
    app.run(debug=True)




