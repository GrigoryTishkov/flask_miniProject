from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Введите имя пользователя",
                           validators=[DataRequired(message="Это поле обязательно для заполнения")],
                           render_kw={"class": "form-control", "placeholder": "Введите имя пользователя"})
    password = PasswordField("Password",
                             validators=[DataRequired(message="Это поле обязательно для заполнения")],
                             render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    remember_me = BooleanField("Remember me", render_kw={"class": "form-check-input"})
    submit_by = SubmitField("Авторизоваться", render_kw={"class": "btn btn-primary"})
    # submit_reg = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-secondary"})


class RegisterForm(FlaskForm):
    username = StringField("Введите имя пользователя",
                           validators=[DataRequired(message="Это поле обязательно для заполнения")],
                           render_kw={"class": "form-control", "placeholder": "Введите имя пользователя"})
    email = StringField("Email", validators=[DataRequired(), Email()],
                        render_kw={"class": "form-control", "placeholder": "Введите почту"})
    password1 = PasswordField("Password",
                              validators=[DataRequired(message="Это поле обязательно для заполнения")],
                              render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    password2 = PasswordField("Repeat password",
                              validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                          EqualTo('Password')],
                              render_kw={"class": "form-control", "placeholder": "Введите пароль"})
    remember_me = BooleanField("Remember me", render_kw={"class": "form-check-input"})
    submit_by = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        pass

    def validate_email(self, email):
        pass
