from db import db 


class PermitModel(db.Model):
    
    __tablename__ = 'permits'#db.Model.metadata.tables['PERMITS']

    PermitType = db.Column(db.String(100))	
    PermitID = db.Column(db.String(50), primary_key = True)	
    IssuedDate = db.Column(db.Date)
    Address	= db.Column(db.String(250))	
    ZipCode	= db.Column(db.Integer)
    Mapsco	= db.Column(db.String(100))
    Contractor = db.Column(db.String(250))
    Value = db.Column(db.String(20))
    Area = db.Column(db.Float)	
    WorkDescription	= db.Column(db.String(500))
    LandUse  = db.Column(db.String(500))



    def __init__(self, permit_type, permit_id, issued_date, 
        address, zipcode, mapsco, contractor,
        value, area, workdescription, landuse):

        self.PermitType = permit_type
        self.PermitID  = permit_id
        self.IssuedDate = issued_date
        self.Address = address
        self.ZipCode = zipcode
        self.Mapsco = mapsco
        self.Contractor = contractor
        self.Value = value
        self.Area = area 
        self.WorkDescription = workdescription
        self.LandUse = landuse

    def json(self):
        """Returns JSON Permit Model Object

            Returns: 
                Dict: Retruns a JSON (Dictionary) of the PermitModel attributes.

        """
        return {'PermitID': self.PermitID, 'IssuedDate': str(self.IssuedDate)
            ,'PermitType': self.PermitType, 'Address': self.Address
            ,'ZipCode': self.ZipCode, 'Mapsco': self.Mapsco
            ,'Contractor': self.Contractor, 'Value': self.Value
            ,'WorkDescription': self.WorkDescription
            ,'LandUse': self.LandUse
            }

    @classmethod 
    def find_by_permit_id(cls, permit_id):
        """Method for queryig the permits DB, by permit ID.

        Args: 
            permit_id (string): Ther permit id for the Dallas Permit.
        
        Returns: 
            class PermitModel: Initializes the PermitModel.  

        """

        return cls.query.filter_by(PermitID = permit_id).first() #limit to 1

