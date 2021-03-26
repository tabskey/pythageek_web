from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import math



# instantiate the app
app = Flask(__name__)
api = Api(app) 
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#array de resultados prévios
results= []   
operation_post_args = reqparse.RequestParser()
operation_post_args.add_argument("numA", type=float, help="A number is required", required=True)
operation_post_args.add_argument("numB", type=float, help="A number is required", required=True)



class LastResult(Resource):
    def get(self):
        if not results:
         response_obj = {'msg': 'Any results registered yet.'}
        else:
         response_obj = results[-1]
        return jsonify(response_obj)
class LastResults(Resource):
    def get(self):
        if not results:
         response_obj = {'msg': 'Any results registered yet.'}
        else:
         response_obj = results[-10:][::-1]    
        return jsonify(response_obj)

class PythaOp(Resource):
     def post(self):
          args = operation_post_args.parse_args()
          a = args["numA"]
          b = args["numB"]
          c = math.sqrt(a**2 + b**2)
          results.append({'number A': int(a), 'number B': int(b), 'result': format(c, ".3f")})
          result_response = {'result': float(format(c, ".3f"))}
          return result_response     
     

# Rotas
api.add_resource(PythaOp,'/theory')
api.add_resource(LastResults, '/last_results')
api.add_resource(LastResult, '/last_result')
    
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)