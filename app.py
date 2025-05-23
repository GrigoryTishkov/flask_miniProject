from flask import Flask, render_template, flash, redirect, url_for, request
from config import Config
from urllib.parse import urlsplit
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm, RegisterForm
from flask_migrate import Migrate
import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User
from extensions import db, login

import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login.init_app(app)
migrate = Migrate(app, db)


# Отладочная функция
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User}


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not urlsplit(next_page).netloc == '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", title="Вход", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('пользователь успешно зарегистрирован!')
        return redirect(url_for("home"))
    return render_template("register.html", title="Регистрация", form=form)


@app.route('/profile/<username>')
@login_required
def profile(username):
    user = db.first_or_404(sa.select(User).where(username == User.username))
    return render_template('profile.html', user=user)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
