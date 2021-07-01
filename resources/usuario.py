from flask_restful import Resource, reqparse
from models.usuario import UserModel
class init(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    atributos.add_argument('imageUrl', type=str, required=True, help="The field 'imageUrl' cannot be left blank.")
    atributos.add_argument('userName', type=str, required=True, help="The field 'userName' cannot be left blank.")
    atributos.add_argument('email', type=str, required=True, help="The field 'email' cannot be left blank.")
    atributos.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank.")

class User(Resource):
   def get(self):
       return {'user': [user.json() for user in UserModel.query.all()]}

class UserDelete(Resource):
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

class UserRegister(Resource):
    # /cadastro
    def post(self):
        dados = init.atributos.parse_args()

        if UserModel.find_by_email(dados['email']):
            return {"message": "The email '{}' already exists.".format(dados['email'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 # Created
    
class UserUpdate(Resource):    
    def put(self, user_id):
        dados = init.atributos.parse_args()
        user = UserModel(**dados)

        user_encontrado = UserModel.find_user(user_id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            user_encontrado.save_user()
            return user_encontrado.json(), 200
        user.save_user()
        return user.json(), 201    


