from typing import TypedDict
from flask import render_template, redirect, url_for, flash

from . import app
from .forms import UserForm


class User(TypedDict):
    first_name: str
    last_name: str
    position: str


USERS = [
    User(
        first_name='Vladislav',
        last_name='Rakityanskiy',
        position='ML engineer'
    )
]


@app.route('/hello_world')
def get_hello_world() -> str:
    return render_template('hello_world.html')


@app.route('/')
@app.route('/index')
def index() -> str:
    return render_template('index.html', users=USERS)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user() -> str:
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = User(
            first_name=user_form.first_name.data,
            last_name=user_form.last_name.data,
            position=user_form.position.data
        )
        USERS.append(user)
        flash(
            f'Added user {user_form.first_name.data} {user_form.last_name.data}, '
            f'position: {user_form.position.data}!'
        )
        return redirect(url_for('index'))

    return render_template('user.html', form=user_form)


