from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
#PitchForm
class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Category pitch')
    submit = SubmitField('Submit')
    #categoryForm
class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()