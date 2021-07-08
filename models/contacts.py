from database import db
from models.user import UserModel

class ContactsModel(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    contactUserId = db.Column(db.Integer, db.ForeignKey('user.id'))

    
    def __init__(self, userId, contactUserId):
        self.userId = userId
        self.contactUserId = contactUserId
        


    def json(self):
        return {k: str(v) for k, v in self.__dict__.items()}

    @classmethod
    def select_all_user_contacts(cls, user_id):
        result = result = db.session.query(
            ContactsModel, UserModel
        ).join(
            UserModel, ContactsModel.contactUserId == UserModel.id
        ).filter(
            ContactsModel.userId == user_id
        ).all()
        response = [{
            'id': x.ContactsModel.contactUserId,
            'name': x.UserModel.name,
        } for x in result]
        return response
    @classmethod
    def find_contact(cls, id):
     return cls.query.filter_by(id=id).first() or None 
    
    def save_contact(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_contact(self):
        db.session.delete(self)
        db.session.commit()    

    def verify_chat_exists(payload, field1, field2):
        result = db.session.query(
            ContactsModel
        
        ).filter(
            ContactsModel.userId == payload[field1], ContactsModel.contactUserId == payload[field2]
        ).all()
        if len(result) != 0:
            return {'message': 'chat already exists'} 
  




