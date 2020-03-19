# RepoReplica

> A flask application used to replicate this repo, thus creating a self replicating repository.

This application can be used to create a link to duplicate this repository in any github users account by going to the link that points to this repo.

## Dependecies
Python 3.7

## Install

The following instructions will allow you to setup your own link either locally or using a domain name to duplicate this repo.
Prior to following these steps ensure that you have python 3.7 installed on your system. 

You will also have to register an application with github.You can do that [here](https://github.com/settings/applications/new) .
When registering your new application you want to make your Homepage URL localhost:5000 and your Authorization callback URL localhost:5000/replicated

### Local Installation Instructions

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
After that last command a webserver will start at localhost:5000 if you go to that link it will then replicate this repo in your github account.

