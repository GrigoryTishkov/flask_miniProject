from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route("/index")
def home():
    now = datetime.datetime.now()
    if 18 <= now.hour < 22:
        greeting = 'Добрый вечер'
    elif 12 <= now.hour < 18:
        greeting = 'Добрый день'
    elif 6 <= now.hour < 12:
        greeting = 'Доброе утро'
    else:
        greeting = 'Доброй ночи'
    return render_template("index.html", title="Главная",  greeting=greeting)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("home"))
    return render_template("login.html", title="Вход", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", title="Регистрация", form=form)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
