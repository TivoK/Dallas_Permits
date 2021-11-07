from flask                import Flask, jsonify
from flask_restful        import Api 
from flask_jwt_extended   import JWTManager
from Resources.Permits    import Permit, PermitList
from Resources.Users      import UserLogin, UserLogOut
from Security.credentials import connection , key 
from Models.Users         import Users
from Models.blocklist     import BlockListModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = key  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =400 
app.config['JWT_BLACKLIST_ENABLED']=True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['refresh','access']

api = Api(app) 

api.add_resource(Permit, '/projects/dallas-permits/permit/<string:permit_id>')
api.add_resource(PermitList,'/projects/dallas-permits/permits/begdate=<string:beg_date>&enddate=<string:end_date>')
api.add_resource(UserLogin, '/projects/dallas-permits/login/')
api.add_resource(UserLogOut, '/projects/dallas-permits/logout/')



jwt = JWTManager(app)  #does not create /auth

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(_decrypted_header, decrypted_body):
    """
    Call back to see if token has been revoked
    """
    jti = decrypted_body['jti']
    block = BlockListModel.get_blocked_jti(jti = jti)
    #create block to iterable check if jti in results
    return jti in str(block)


@jwt.revoked_token_loader
def revoked_token_callback(_decrypted_header, _decrypted_body):
    return jsonify({'message': 'Access token has been revoked.'
                    ,'error': 'Blocked Token Used.'}), 401


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

