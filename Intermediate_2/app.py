from flask import Flask, render_template, request
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

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form or None)
    context = {
        'form': form,
    }

    if form.validate_on_submit():  # this method is available in `from flask.ext.wtf import Form`
    # if request.method == 'POST' and form.validate():
        context['form_data'] = form.data

    return render_template('register.html', **context)

if __name__ == '__main__':
    app.secret_key = 'SECRET_KEY'
    app.run(debug=True)
