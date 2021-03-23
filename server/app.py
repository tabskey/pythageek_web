from flask import Flask, jsonify, request
from flask_cors import CORS
import math



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#array de resultados prévios
results= []

# sanity check route
# @app.route('/theory', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')

# @app.route('/theory', methods=['GET']) ## mudara pra results
# def last_results():
#     if not results:
#         response_obj = {'msg': 'Sem resultados no momento.'}
#     else:
#         response_obj = results[-1]    
#     return jsonify(response_obj)


@app.route('/theory/<numA>/<numB>', methods=['GET'])
def pythagorean_theorem(numA,numB):
     a = float(numA)
     b = float(numB)
     c = math.sqrt(a**2 + b**2)
     return jsonify(c)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)