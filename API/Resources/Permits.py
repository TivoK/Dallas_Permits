import sqlalchemy
from datetime import datetime
from flask_restful import Resource, reqparse 
from Models.Permits import PermitModel



class Permit(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'permit_id'
        ,type = str
        ,required = True 
        ,help = 'permit_id cannot be blank.'
    )

   

    def get(self, permit_id):
        permit = PermitModel.find_by_permit_id(permit_id)
        if permit:
            return permit.json()
        return {'message' : f'PermitID: {permit_id} not found'}, 404


class PermitList(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'beg_date'
        ,type = str 
        ,required = True
        ,help = 'Begin date required.'
    )

    parser.add_argument(
        'end_date'
        ,type = str
        ,required = True
        ,help = 'End Date required'
    )

    def get(self, beg_date, end_date):
        try: 
            format = '%Y-%m-%d'
            [datetime.strptime(x,format) for x in [beg_date,end_date]]
            permits  = PermitModel.find_permits_by_date(beg_date, end_date)
            return {'permits': [x.json() for x in permits]}
        except ValueError:
            return {'message' : 'Invalid Dates. Dates should be formatted YYYY-MM-DD.'}
       # return {'message': 'No permits found for specified range.'}




