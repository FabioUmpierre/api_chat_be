from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    imageUrl = db.Column(db.String(40))
    userName = db.Column(db.String(40))
    email = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, name, imageUrl, userName, email, password):
        self.name = name
        self.imageUrl = imageUrl
        self.userName = userName
        self.email = email
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'imageUrl': self.imageUrl,
            'userName': self.userName,
            'email': self.email
            }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_user (self, name, imageUrl, userName, email, password):
        self.name = name
        self.imageUrl = imageUrl
        self.userName = userName
        self.email = email
        self.password = password 
