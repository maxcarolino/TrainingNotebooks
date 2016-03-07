from flask import Flask, flash, redirect, render_template, request, url_for
from flask.ext.wtf import Form
from wtforms import PasswordField, TextField, validators
app = Flask(__name__)


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('register1')
    form = RegistrationForm(request.form or None)
    print('register2')

    # if request.method == 'POST' and form.validate():
    if form.validate_on_submit():  # this method is available in `from flask.ext.wtf import Form`
        print('register3')

        # do something with the data
        # here, we use it to instantiate and save an imaginary User object
        print(dir(form))
        # user = User(form.username.data, form.email.data, form.password.data)
        # user.save()

        # flash('Thanks for registering')
        print('register4')
        return redirect(url_for('login'))

    print('register5')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.secret_key = 'SECRET_KEY'
    app.run(debug=True)
