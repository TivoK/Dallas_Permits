from flask             import Flask 
from flask_restful     import Api 
from Resources.Permits import Permit

app = Flask(__name__)
api = Api(app) 

api.add_resource(Permit, '/permit/<string:permit_id>')

app.run(port = 5000, debug = True)


