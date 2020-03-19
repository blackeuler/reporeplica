from flask import Flask 
from authlib.integrations.flask_client import OAuth
from os import getenv,urandom

app = Flask(__name__)
app.config.update(SECRET_KEY=urandom(24))

oauth = OAuth(app)

clientId = getenv("CLIENT_ID")
clientSecret = getenv("ClIENT_SECRET")


oauth.register(
    name='github',
    client_id=clientId,
    client_secret=clientSecret,
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'repo'},
)


@app.route('/')
def index():
    return 'Hello World'