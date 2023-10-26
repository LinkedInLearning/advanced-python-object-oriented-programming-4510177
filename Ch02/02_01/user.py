# %% Auth
class Auth:
    def __init__(self, db):
        self.db = db

    def from_token(self, token):
        return self.db.get(token)

auth = Auth({
    'b92d877': 'carly',
    '18317ac': 'elliot',
})


# %% User
class User:
    def __init__(self, login):
        self.login = login
        # TODO: More fields

    @classmethod
    def from_token(cls, token):
        login = auth.from_token(token)
        return cls(login)

## %% Admin
class Admin(User):
    ...  # TODO
    

# %% Test
u = User('carly')
print(u.login, type(u))

u = User.from_token('b92d877')
print(u.login, type(u))

a = Admin.from_token('18317ac')
print(a.login, type(a))
