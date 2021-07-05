from flask import Flask
from flask_restful import Api
from resources.usersearch import UserSearch
from resources.userlist import UserList
from resources.usercrud import UserCrud

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    db.create_all()

api.add_resource(UserList, '/user')                         
api.add_resource(UserCrud, '/user/<int:id>')          
api.add_resource(UserSearch, '/user/search/<string:name>')      

if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(debug=True)
