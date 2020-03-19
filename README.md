# RepoReplica

> A flask application used to replicate this repo, thus creating a self replicating repository.

This application can be used to create a link to duplicate this repository in any github users account by going to the link that points to this repo.

## Install

The following instructions will allow you to setup your own link either locally or using a domain name to duplicate this repo.

```sh
# Let's clone this repository
git clone https://github.com/blackeuler/reporeplica.git
# Then change directory 
cd reporeplica
# At this point we need to install the dependencies using pip.
#You can use pip or pipenv but I recommend using pipenv.
pipenv install
# Afterwards you need to set your client key and secret key from Github as a environment variable
export CLIENT_ID = "your client id"
export CLIENT_SECRET = "your client secret"
# Finnaly to get the flask app running you need to set the flask environement variable
export FLASK_APP = app.py
# Now you can run the application
flask run
```

