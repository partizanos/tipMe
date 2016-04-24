from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import mongoengine
# ...
from pymongo import MongoClient
from django.template import Context, loader
def index(request):
	server="localhost"
	port = 27017
	c = MongoClient()
	db=c.yelp
	collection = db['tip']

	template = loader.get_template("polls/generic.html")
	return HttpResponse(template.render())

def db_req(request):
	server="localhost"
	port = 27017
	c = MongoClient()
	db=c.yelp
	collection = db['tip']
	return HttpResponse(str(collection.find_one()))
    # return HttpResponse("Hello, world. You're at the polls index.")

#Establish a connection with mongo instance.
# conn = Connection(server,port)
# assert isinstance(user, mongoengine.django.auth.User)
