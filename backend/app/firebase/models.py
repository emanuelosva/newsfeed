"""File of models"""

#flask
from flask_login import UserMixin
#Firestore_service
from firestore_service import get_user_by_email

class UserData():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.email
        self.password = user_data.password
    
    @staticmethod
    def query(user_id)
    user_validation = get_user_by_email(user_id)
    user_data = UserData(
        email = user_validation.id,
        username = user_validation.to_dict()['username']
        password = user_validation.to_dict()['password']
    )
    return UserModel(user_data)