from marshmallow import Schema, fields, validate

class UserLoginSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, load_only=True)

class UserSchema(UserLoginSchema):
    name = fields.Str(required=True)
    last_name = fields.Str(required=False)
    
class UserTokensSchema(Schema):
    access_token = fields.Str(required=False, dump_only=True)
    refresh_token = fields.Str(required=False, dump_only=True)
    user = fields.Nested(UserSchema(), dump_only=True)
    
class UserCategories(Schema):
    categories = fields.List(fields.Str(), required=True)
    
class UserRecomendQuestion(Schema):
    question = fields.Str(required=True)
    
class QuestionsGenerated(Schema):
    questions = fields.List(fields.Str(), required=True)
