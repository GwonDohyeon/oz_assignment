from marshmallow import Schema, fields

class BoardSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str()
    user_id = fields.Int(required=True)
    author = fields.Nested('UserSchema', exclude=('boards',))  # `author`는 `UserSchema`로 중첩, 순환 참조 방지
