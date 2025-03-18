from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder":
    "Введите имя пользователя"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder":
    "Введите пароль"})
    remember_me = BooleanField("Remember me", validators=[DataRequired()], render_kw={"class": "form-check-input"})
    submit_by = SubmitField("Авторизоваться", render_kw={"class": "btn btn-primary"})
    submit_reg = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-secondary"})


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder":
        "Введите имя пользователя"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder":
        "Введите пароль"})
    email = StringField("Email", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder":
        "Введите почту"})
    submit_by = SubmitField("Авторизоваться", render_kw={"class": "btn btn-primary"})
