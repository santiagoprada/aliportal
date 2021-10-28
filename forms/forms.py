from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
    usuario = StringField("usuario", validators=[DataRequired(message="este campo es requerido")])
    contraseña = PasswordField("contraseña", validators=[DataRequired(message="este campo es requerido")])
    recordar = BooleanField("recordar usuario")

