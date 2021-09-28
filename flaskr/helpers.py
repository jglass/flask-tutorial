from wtforms import Form, BooleanField, StringField, PasswordField, validators

class GamesForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=250)])
    author = StringField('Author', [validators.Length(min=1, max=199)])
    image_url = StringField('Image Url', [validators.Length(min=1, max=350)])
    type = StringField('Type', [validators.Length(min=1, max=35)])
