import json
from flask import Flask, render_template, url_for, redirect
from flask.views import MethodView

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Respond with a Hello World string."""
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    """Respond with a Hello name variable in a string with a link."""
    return 'Hello <a href="{}">{}! '.format(url_for('hello_marquee', name=name), name.capitalize())


@app.route('/<name>/')
def hello_marquee(name):
    """
    Respond with a Hello name in HTML (with a <marquee>!).

    Add all variables into context.
    Get template from /templates.
    Interpolate variables into the HTML.
    Return the result.
    """
    context = {
        'name': name.capitalize()
    }
    return render_template('hello.html', **context)


@app.route('/error')
def error():
    """Return nothing. Responds with the debugger screen."""
    #return
    return redirect(url_for('hello_world'))


class API(MethodView):
    """Class-based view demo."""

    def get(self, arg):
        """Return arg data."""
        data = {'arg': arg}
        return json.dumps(data)

    def post(self):
        """Return 'OK'."""
        return 'OK'

app.add_url_rule('/api/<arg>', view_func=API.as_view('api'))


if __name__ == '__main__':
    app.run(
        debug=True,
        host="localhost",
        port=8000,
    )
