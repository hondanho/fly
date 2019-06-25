
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        return {'employees': '1'} 
    
class Tracks(Resource):
    def get(self):
        result = {'data': '2'}
        return jsonify(result)
    
class Employees_Value(Resource):
    def get(self, employee_id):
        result = {'data': employee_id}
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Value, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
     app.run(port=3000)
