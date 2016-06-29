uthor__ = 'hochikong'
from flask import Flask,request
from flask.ext.restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)

todos = {'task':'get the list of docker'}

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,help='get the name')


class TodoSimple(Resource):
    def get(self,todo_id):
        args = parser.parse_args()
        if args['auth-token'] == 'thisismytoken':
            return {todo_id:todos[todo_id]}
        else:
            return {'error':'token error'},401

    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

class GetName(Resource):
    def post(self):
        args = parser.parse_args()
        name = args['name']
        #name = {}
        #name['ac'] = args['name']
        #name = request.json.get('name')
        return {'yourame':name}

api.add_resource(TodoSimple,'/<string:todo_id>')
api.add_resource(GetName,'/getname')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9100)
