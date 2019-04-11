from flask import Flask, request, redirect, render_template
import cgi
import os
import re 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup_form.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)


@app.route('/', methods=['POST'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    did_error = False

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        did_error = True
        username_error = 'This is not a valid username'
    if ' ' in username:
        did_error = True
        username_error = 'This is not a valid username - no spaces please'
    if len(username) < 3 or len(username) > 20:
        did_error = True
        username_error = 'This is not a valid username - must be between 3 and 20 characters'

    if password == '':
        did_error = True
        password_error = 'This is not a valid password'
    if ' ' in password:
        did_error = True
        password_error = 'This is not a valid password - no spaces please'
    if len(password) < 3 or len(password) > 20:
        did_error = True
        password_error = 'This is not a valid password - must be between 3 and 20 characters'

    if verify_password != password:
        did_error = True
        verify_password_error = 'This password does not match your previous entry'

    if email != '':
        if not re.match(r'^[^@ ]+@[^@ ]+\.[^@ ]+$', email):
            did_error = True
            email_error = 'This is not a valid email'
        if len(email) < 3 or len(email) > 20:
            did_error = True
            email_error = 'This is not a valid email - must be between 3 and 20 characters'

    
    if did_error == True:
        return render_template('signup_form.html', 
                                username=username, 
                                email=email, 
                                username_error=username_error, 
                                password_error=password_error, 
                                ver_password_error=verify_password_error,
                                email_error=email_error)
    else:
        return redirect('/welcome', code=307)

    


    








app.run()