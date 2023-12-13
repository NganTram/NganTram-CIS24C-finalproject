from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import StringField, validators

class TrigForm(FlaskForm):
    function_name = SelectField('Function', 
                                choices=[('sin', 'Sin'), ('cos', 'Cos'), ('tan', 'Tan'), ('cot', 'Cot')],
                                validators=[DataRequired()])
    custom_function = StringField('Custom Function', validators=[validators.Optional()])
    action = SelectField('Action',
                         choices=[('plot', 'Plot Function'), ('inverse', 'Plot Inverse'), ('domain_range', 'Find Domain and Range'), ('asymptotes', 'Find Asymptotes')],
                         validators=[DataRequired()])
    submit = SubmitField('Visualize')
