from db import db 

class Users (db.Model):
    
    ___tablename__= 'users'
   
    UserID = db.column(db.Integer,primary_key=True)
    UserName = db.column(db.String(50))
    UserPassword = db.Column(db.String(50))
    UserType = db.Column(db.String(10))
   

    def __init__(self, UserName, UserPassword):
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.UserType = 'GUEST'

    def json (self):
        return {
             'UserID': self.UserID
            ,'UserName': self.UserName
        }

    @classmethod
    def find_user_id(cls):
        """ Returns User ID Record if found from Users Table
        Args: None

        Return: Dict Query Output JSON Format
        """
        return cls.query.filter_by(UserID = UserID)

    @classmethod 
    def find_user_name(cls):
        """ Returns UserName Record if found from Users Table
        Args: None
        
        Return: Dict Query Output JSON Format
        """
        return cls.query.filter_by(UserName = UserName)
