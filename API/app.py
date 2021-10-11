from flask                import Flask 
from flask_restful        import Api 
from flask_jwt_extended   import JWTManager
from Resources.Permits    import Permit, PermitList
from Resources.Users      import UserLogin
from Security.credentials import connection , key 
from Models.Users import Users



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = key  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =60 #for now, tokens only last for 1 min (60 secs)
api = Api(app) 

api.add_resource(Permit, '/permit/<string:permit_id>')
api.add_resource(PermitList,'/permits/begdate=<string:beg_date>&enddate=<string:end_date>')
api.add_resource(UserLogin, '/login/')


jwt = JWTManager(app)  #does not create /auth

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

