from flask_restful import Resource, reqparse
from models.contacts import ContactsModel
class receive_attribute(Resource):
    atributes = reqparse.RequestParser()
    atributes.add_argument('userId', type=int, required=True, help="The field 'userId' cannot be left blank.")
    atributes.add_argument('contactUserId', type=int, required=True, help="The field 'contactUserId' cannot be left blank.")


class ContactSearch(Resource):
    def get(self,user_id):
        result = ContactsModel.select_all_user_contacts(user_id)
        return result

class ContactList(Resource):   
    def post(self):
        payload = receive_attribute.atributes.parse_args() 
        result = ContactsModel.verify_chat_exists(payload,'userId','contactUserId')
        if result:
            return result
            
        contact = ContactsModel(**payload)
        contact.save_contact()

        result = ContactsModel.verify_chat_exists(payload,'contactUserId','userId')
        if result:
            return result
        
        contact = ContactsModel(payload['contactUserId'],payload['userId'])
        contact.save_contact()
        return {'message': 'contact added is succefully!'}  

class ContactDelete(Resource):
    def delete(self,id):
        contacts = ContactsModel.find_contact(id)
        if contacts:
            contacts.delete_contact()
            return {'message': 'contact deleted.'}
        return {'message': 'contact not found.'}, 404
      
        
     
            