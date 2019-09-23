from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    #PitchForm
class PitchForm(FlaskForm):

    content = TextAreaField('Your Pitch',validators=[Required()])
    submit = SubmitField('Submit')
    #categoryForm
class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()
    #Comment Form

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    opinion = TextAreaField('Write your comment')
    submit = SubmitField('Submit')
    


class UpvoteForm(FlaskForm):
    
    
    submit = SubmitField('Upvote')

class DownvoteForm(FlaskForm):
    
    
    submit = SubmitField('Downvote')