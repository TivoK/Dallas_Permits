from flask_restful import Resource, reqparse 


class Permit(Resource):

    parser = reqparse.RequestParser()

    parser = reqparse.add_argument(
        'permit_id'
        ,type = str
        ,required = True 
        ,help = 'permit_id cannot be blank.'
    )
    
    
    def get(self, permit_id):
        return {'permit_id':permit_id}

    


