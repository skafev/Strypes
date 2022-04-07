class Users:
    def __init__(self, name, username, password, gender, role, id=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.role = role

    def __str__(self):
        return f'{self.id}) {self.name} {self.username}: {self.role}'

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.name:15.15s} ' \
               f'| {self.username:15.15s} ' \
               f'| {self.gender:3s} ' \
               f'| {self.role:18.18s}'
