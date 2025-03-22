from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from extensions import db
from models import User


class LoginForm(FlaskForm):
    username = StringField("Введите имя пользователя",
                           validators=[DataRequired(message="Это поле обязательно для заполнения")],
                           render_kw={"class": "form-control", "placeholder": "Введите имя пользователя"})
    password = PasswordField("Password",
                             validators=[DataRequired(message="Это поле обязательно для заполнения")],
                             render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    remember_me = BooleanField("Remember me", render_kw={"class": "form-check-input"})
    submit_by = SubmitField("Авторизоваться", render_kw={"class": "btn btn-primary"})


class RegisterForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(message="Это поле обязательно для заполнения")],
                           render_kw={"class": "form-control", "placeholder": "Введите имя пользователя"})
    email = StringField("Email", validators=[DataRequired(message="Это поле обязательно для заполнения"), Email()],
                        render_kw={"class": "form-control", "placeholder": "Введите почту"})
    password = PasswordField("Password",
                             validators=[DataRequired(message="Это поле обязательно для заполнения")],
                             render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    password2 = PasswordField("Repeat password",
                              validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                          EqualTo('password', message="Пароли не совпадают")],
                              render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    submit_by = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-primary"})


    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Такое имя пользователя уже существует.')


    def validate_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email is not None:
            raise ValidationError('Такой Email уже существует.')
