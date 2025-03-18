from flask import Flask, render_template, redirect, url_for
from config import Config
from forms import LoginForm, RegisterForm
import datetime

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    now = datetime.datetime.now()
    if 18 <= now.hour < 22:
        greeting = 'Добрый вечер'
    elif 12 >= now.hour < 18:
        greeting = 'Добрый день'
    elif 6 >= now.hour < 12:
        greeting = 'Доброе утро'
    else:
        greeting = 'Доброй ночи'
    return render_template("index.html", title="Главная",  greeting=greeting)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
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
