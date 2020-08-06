"""Logic of background of forms"""

class SignupForms():
    def __init__(self, username, email, password, passwd_confirm):
        self.username = username
        self.email = email
        self.password = password
        self.passwd_conf = passwd_confirm

    def validate_passwords(self):
        """Comparate password and password confirmation from signup form,
        return boolean data type.
        """
        if self.password == self.passwd_confirm:
            return True
        else:
            return False 
