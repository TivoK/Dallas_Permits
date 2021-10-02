from flask                import Flask 
from flask_restful        import Api 
from Resources.Permits    import Permit, PermitList
from Resources.Users      import UserLogin
from Security.credentials import connection
from Models.Users import Users



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app) 

api.add_resource(Permit, '/permit/<string:permit_id>')
api.add_resource(PermitList,'/permits/begdate=<string:beg_date>&enddate=<string:end_date>')
api.add_resource(UserLogin, '/login/')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

