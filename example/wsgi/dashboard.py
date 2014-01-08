import os

from flask import Flask, render_template

from flask_appconfig import AppConfig
from flask.ext.bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required

from marconiclient.queues.v1 import client

URL = "http://%s:%s/v1" % (os.environ.get('OPENSHIFT_MARCONI_HOST', '127.0.0.1'),
                           os.environ.get('OPENSHIFT_MARCONI_PORT', 8888))


class PostMessage(Form):
    queue = TextField('Queue', description='Queue Name',
                      validators=[Required()])
    message = TextField('Message', description='Post a message to the queue',
                        validators=[Required()])
    submit_button = SubmitField('Submit Form')


def create_app(configfile=None):
    app = Flask(__name__)
    app.debug = True
    AppConfig(app, configfile)
    Bootstrap(app)
    app.config['SECRET_KEY'] = 'devkey'
    return app


app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostMessage()

    if form.validate_on_submit():
        mclient = client.Client(URL)
        msg = {'body': form.message.data, 'ttl': 60}
        mclient.queue(form.queue.data).post([msg])

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
