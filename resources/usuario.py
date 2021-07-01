from flask_restful import Resource, reqparse
from models.usuario import userModel
class receive_atribute(Resource):
    atributes = reqparse.RequestParser()
    atributes.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    atributes.add_argument('imageUrl', type=str, required=True, help="The field 'imageUrl' cannot be left blank.")
    atributes.add_argument('userName', type=str, required=True, help="The field 'userName' cannot be left blank.")
    atributes.add_argument('email', type=str, required=True, help="The field 'email' cannot be left blank.")
    atributes.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank.")

class user(Resource):
   def get(self):
       return {'user': [user.json() for user in userModel.query.all()]}

class userDelete(Resource):
    def delete(self, user_id):
        user = userModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

class userRegister(Resource):
    def post(self):
        data = receive_atribute.atributes.parse_args()

        if userModel.find_by_email(data['email']):
            return {
                        "message": "The email '{}' already exists.".format(data['email'])
                   }

        user = userModel(**data)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 
    
class userUpdate(Resource):    
    def put(self, user_id):
        data = receive_atribute.atributes.parse_args()
        user = userModel(**data)

        user_found = userModel.find_user(user_id)
        if user_found:
            user_found.update_user(**data)
            user_found.save_user()
            return user_found.json(), 200
        user.save_user()
        return user.json(), 201    


