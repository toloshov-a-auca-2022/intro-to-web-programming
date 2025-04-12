from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class FabricForm(FlaskForm):
    name = StringField('Fabric Name', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    quantity = IntegerField('Quantity (meters)', validators=[DataRequired()])
    submit = SubmitField('Add Fabric')
