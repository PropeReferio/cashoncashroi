from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class ROIForm(FlaskForm):
    #Income
    rent = StringField("Rent", validators=[DataRequired()])
    other = StringField("Other Income", validators=[DataRequired()])
    #Monthly Expenses
    mortgage = StringField("Mortage Payment", validators=[DataRequired()])
    tax = StringField("Taxes", validators=[DataRequired()])
    insur = StringField("Insurance", validators=[DataRequired()])
    util = StringField("Utilities", validators=[DataRequired()])
    hoa = StringField('HOA Fees', validators=[DataRequired()])
    lawnsnow = StringField('Lawn/Snow', validators=[DataRequired()])
    vacancy = StringField('How much would you like to save each month to prepare \
for a vacancy?', validators=[DataRequired()])
    repairs = StringField('Repairs', validators=[DataRequired()])
    capex = StringField('Capex', validators=[DataRequired()])
    management = StringField('Property Management', validators=[DataRequired()])
    #Initial Investment
    down = StringField('Down Payment', validators=[DataRequired()])
    closing = StringField('Closing Costs', validators=[DataRequired()])
    maint = StringField('Initial maintenance', validators=[DataRequired()])
    misc = StringField('Other miscellaneous costs', validators=[DataRequired()])

    submit = SubmitField("Submit")