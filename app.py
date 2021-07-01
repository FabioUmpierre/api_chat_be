from flask import Flask
from flask_restful import Api
from resources.usuario import user, userRegister, userDelete, userUpdate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    db.create_all()

api.add_resource(user, '/users')
api.add_resource(userRegister, '/register')
api.add_resource(userDelete, '/users/<int:user_id>')
api.add_resource(userUpdate, '/users/<int:user_id>')

if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(debug=True)
