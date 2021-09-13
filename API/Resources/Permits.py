import sqlalchemy
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





