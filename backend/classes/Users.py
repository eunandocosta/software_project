from marshmallow import Schema, fields, ValidationError

class User(object):
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __repr__(self):
        return '<User(email={self.email!r}) User(senha={self.senha!r})>'.format(self=self)
    
class UserSchema(Schema):
    email = fields.Str()
    senha = fields.Str()

class UserLogin(object):
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __repr__(self):
        return '<User(email={self.email!r}) User(senha={self.senha!r})>'.format(self=self)
    
class UserLoginSchema(Schema):
    email = fields.Str()
    senha = fields.Str()
