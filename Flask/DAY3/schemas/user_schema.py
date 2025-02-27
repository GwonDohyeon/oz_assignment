from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # `id`는 읽기 전용
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    boards = fields.List(fields.Nested('BoardSchema', exclude=('author',)))  # 관계를 명시적으로 포함