from flask import Flask, url_for 
from authlib.integrations.flask_client import OAuth
from os import getenv,urandom

app = Flask(__name__)
app.config.update(SECRET_KEY=urandom(24))

oauth = OAuth(app)

clientId = getenv("CLIENT_ID")
clientSecret = getenv("CLIENT_SECRET")

print(clientId)
print(clientSecret)
oauth.register(
    name='github',
    client_id=clientId,
    client_secret=clientSecret,
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'public_repo'},
)


@app.route('/')
def index():
    redirect_uri = url_for('replicated', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)

@app.route('/replicated')
def replicated():
    token = oauth.github.authorize_access_token()
    resp = oauth.github.post('repos/blackeuler/reporeplica/forks')
    return 'Repository Replicated'