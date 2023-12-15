from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import forms
import requests

app_blueprint = Blueprint('routes', __name__,  template_folder='templates')

@app_blueprint.route('/')
@app_blueprint.route('/home')
def home():
    return render_template("home/index.html")

@app_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    form = forms.LoginForm(request.form)
    if form.validate_on_submit():
        if form.username.data == 'majid@gmail.com' and form.password.data == '12345':
            flash(f'Login successful for {form.username.data}', category='success') 
            return redirect('home')
        else:
            flash(f'Login unsuccessful for {form.username.data}', category='danger')
    return render_template("login/login.html", title='Login', form=form) 

@app_blueprint.route('/register')
def register():
    return render_template("register/register.html")


@app_blueprint.route('/product')
def product():
    return render_template("home/index.html")            