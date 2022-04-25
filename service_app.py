from flask import Flask
import flask_restful


from controllers.ping import Ping
from controllers.brands import Brand

app = Flask(__name__)
api = flask_restful.Api(app)

api = flask_restful.Api(app, prefix='/simpleflaskservice/v1/')

api.add_resource(Ping, 'ping/', 'ping/<string:id>')
api.add_resource(Brand, 'master/brand/', 'master/brand/<string:id>')



if __name__ == '__main__':
    app.run(debug=True)
