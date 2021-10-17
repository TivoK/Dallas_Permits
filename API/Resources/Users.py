from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from Models.Users import Users
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt)

from Models.blocklist import BlockListModel

_user_data_parser = reqparse.RequestParser()

_user_data_parser.add_argument(
                     'username'
                     ,type = str
                     ,required = True
                     ,help ='UserName cannot be blank'     
                    )

_user_data_parser.add_argument(
                    'password'
                    ,type = str 
                    ,required = True
                    ,help = 'Password argument is required.'

)

class UserLogin(Resource):
    @classmethod

    def post(cls):
        """
        This class method will login the user and send a confirmation message.
        Args: None

        Return: Dict w/ formatted Query results in JSON format.
    
        """
        #gets the parser data that is passed.
        data = _user_data_parser.parse_args()
 
        user = Users.find_user_name(data['username'])
        
        if user and safe_str_cmp(user.UserPassword, data['password']):
            token = create_access_token(identity = user.UserName, fresh = True)
            return {'token': token, 'message': 'User Login Successful.'}, 200
        return {'message': 'Invalid Credentials submitted.'}, 401


class UserLogOut(Resource):
    
    @jwt_required()
    def post(self):
        """Adds JTI to the Block List Upon Logout.
        Args: None

        Returns: (Dict) Json object of logout.
    
        """
        jti = get_jwt()['jti']
        identity = get_jwt_identity()
        #create block list class 
        Blocked = BlockListModel(identity = identity, jti =jti)
        Blocked.add_to_blocklist()
        
        return {'message': f'Logout Sucessfull for {identity}. Token has been added'\
            f' to block list.'
            ,'token':jti
            }, 200