from flask import Flask
from flask_restful import Api
from resources.usuario import User, UserRegister, UserDelete, UserUpdate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_db():
    db.create_all()

api.add_resource(User, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(UserDelete, '/users/<int:user_id>')
api.add_resource(UserUpdate, '/users/<int:user_id>')
if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
