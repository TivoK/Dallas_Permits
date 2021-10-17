from datetime import datetime 
from datetime import timezone
from db import db

class BlockListModel(db.Model):
    __tablename__ = 'blocklist'

    identity = db.Column(db.String(500))
    jti = db.Column(db.String(500), primary_key =True)
    blockdate = db.Column(db.DateTime)

    def __init__(self,identity,jti):
        self.identity = identity
        self.jti = jti 
        self.blockdate = datetime.now(timezone.utc)

    def json(self):
        """
        Returns the Json Object of the BlockListModel Class

        Args: None
        
        Returns: (Dict) the Json Object of the BlockListModel Class
        """
        return {
            'identity':self.identity
            ,'jti':self.jti
            ,'blockdate': self.blockdate
        }

    def add_to_blocklist(self):
        """
        Saves JTI/Identity to DB blocklist.
        
        Args: None

        Returns: None. Saves JTI/Identity to DB

        """
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_blocked_jti(cls,jti):
        """Returns  a JTI if it is listed in blocklist db
        Args: (String) JTI to lookup

        Returns: Returns Record if JTI is found
        """
        return cls.query.filter_by(jti = jti).first()
