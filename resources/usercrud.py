from flask_restful import Resource
from models.user import UserModel
from resources.user import receive_attribute

class UserCrud(Resource):
    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    def delete(self,id):
        user = UserModel.find_user(id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404
    
    def patch(self,id):
        payload = receive_attribute.atributes.parse_args()
        user = UserModel(**payload)

        user_found = UserModel.find_user(id)
        if user_found:
            user_found.update_user(**payload)
            user_found.save_user()
            return user_found.json(), 200
        user.save_user()
        return user.json(), 201    