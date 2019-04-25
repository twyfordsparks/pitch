from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class PitchForm1(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('Funny','Funny')])
    submit = SubmitField('Submit')

class PitchForm2(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('PickupLine','PickupLine')])
    submit = SubmitField('Submit')

class PitchForm3(FlaskForm):
    pitch = TextAreaField('Pitch Comment', validators=[Required()])
    my_category = SelectField('Category', choices=[('Cheesy','Cheesy')])
    submit = SubmitField('Submit')
