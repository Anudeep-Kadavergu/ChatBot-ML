import app.main
import flask
from flask import request, jsonify
from flask_cors import CORS



application = flask.Flask(__name__)
application.config["DEBUG"] = True
CORS(application)

@application.route('/', methods=['GET'])
def home():
    return ""

@application.route('/api/v1/resources', methods=['GET'])
def api_id():
    if 'id' in request.args and 'user' in request.args:
        id = request.args['id']     
        user = request.args['user']
        if user not in app.main.users: 
            app.main.users.update( {user : [0,'NULL']} )
    else:
        return "Error: No id field provided. Please specify an id."
    msg = app.main.send(id,user)
    return str(msg)

if __name__ == "__main__": 
    application.run(port=5000, debug=True)
