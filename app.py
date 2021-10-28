import os

from flask.helpers import flash
from  forms.forms import *
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if (form.validate_on_submit()):
        usuario = form.usuario.data
        flash(f"bienvenido(a) {usuario}")
        return redirect(url_for('admindash'))    
    return render_template('login.html', form=form)

@app.route('/emp')
def empdash():
    return render_template('emp.html')

@app.route('/admin', methods=['GET', 'POST'])
def admindash():
    return render_template('admin.html')

@app.route('/superadmin')
def superadmindash():
    return render_template('superadmin.html')