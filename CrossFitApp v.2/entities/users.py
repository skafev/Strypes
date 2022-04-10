class Users:
    def __init__(self, first_name, last_name, username, password, gender, role, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gender = gender
        self.role = role

    def __str__(self):
        return f'{self.id}) {self.first_name} {self.last_name} {self.username}: {self.role}'

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.first_name:15.15s} | {self.last_name:15.15s}' \
               f'| {self.username:15.15s} ' \
               f'| {self.gender:3s} ' \
               f'| {self.role:18.18s}'
