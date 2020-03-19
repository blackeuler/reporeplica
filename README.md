# RepoReplica

> A flask application used to replicate this repo, thus creating a self replicating repository.

This application can be used to create a link to duplicate this repository in any github users account by going to the link that points to this repo.

Here is a deployed heroku link for the application: [link](https://reporeplica.herokuapp.com/)

## Dependecies
Python 3.7

## Install

The following instructions will allow you to setup your own link either locally or using a domain name to duplicate this repo.
Prior to following these steps ensure that you have python 3.7 installed on your system. 

You will also have to register an application with github.You can do that [here](https://github.com/settings/applications/new) .
When registering your new application you want to make your Homepage URL localhost:5000 and your Authorization callback URL localhost:5000/replicated

### Local Installation Instructions(Linux/Mac)

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

## Deploy
While there are many ways to deploy a flask application I believe the easiest is [Heroku](http://heroku.com/).
You can make an account there and it will link to your github account. You can deploy directly from the repository.
In order to make the application work you need to set the environemnt variables in your heroku project just like in the local installation.

Another thing that needs to be changed is in your github settings once Heroku gives you a domain name you will either need to register a new
application with Github or you will need to change the Homepage URL and the Authorization Callback URL to match the URL that heroku will give you.
You need a CLIENT_ID, and CLIENT_SECRET. Once you have those environement variables set the application will run as expected.



## How it Works

This application is a flask application. Flask is a micro-webframework written in python. It allows you to start servers and build websites
using only a small amount of tools.You then have the option of adding more functionality as your application needs them. You can learn more about flask [here](https://flask.palletsprojects.com/en/1.1.x/) Our flask app uses an open source library for handling OAuth with Github called [Authlib](https://authlib.org). 
Using OAuth the user goes to our link and then starts the authentication process with Github, the permission the app asks for is read/write acces to public repos. Once we have the authentication token from github we utilize the [Github API](https://developer.github.com/v3/) to then fork this repository in the authenticated users account thus replicated this repo.

