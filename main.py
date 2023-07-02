from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json

app = Flask(__name__)
api = Api(app)

#/users
users_path = './data/users.csv'
#/locations
locs_path = './data/locations.csv'
class Users(Resource):
    def get(self):
        data = pd.read_csv(users_path)
        data = data.to_dict()
        return {'data': data}, 200
    


class Locations(Resource):
    def get(self):
        data = pd.read_csv(locs_path)
        data = data.to_dict()
        return {'data': data}, 200

#api.com/users
api.add_resource(Users, '/users')
#api.com/locations
api.add_resource(Locations, '/locations')

if __name__ == "__main__":
    app.run(debug=True)




