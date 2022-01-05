class students:
    count_id = 0

    def __init__(self, name, username, email, password, confirmpass):
        students.count_id += 1

        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.confirmpass = confirmpass

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_confirmpass(self):
        return self.confirmpass

    def set_name(self, name):
        self.name = name

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_confirmpass(self, confirmpass):
        self.confirmpass = confirmpass
