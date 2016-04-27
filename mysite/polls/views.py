# from django.shortcuts import render
from django.http import HttpResponse
# import mongoengine
from pymongo import MongoClient
from django.template import loader


def index(request):
    # server = "localhost"
    # port = 27017
    # c = MongoClient()
    # db = c.yelp
    # collection = db['tip']

    template = loader.get_template("polls/generic.html")
    return HttpResponse(template.render())


def db_req(request):
    if request.method == 'GET':
        c = MongoClient()
        db = c.yelp
        collection = db['ptip']
        value = request.GET.get('value').encode('utf8')
        # collection = db['tip']
        # return HttpResponse(request.body)
        # db.ptip.find( { nouns: { $elemMatch: { "name" : "bakery" } } } )
        totalPtips = []
        i = 0
        string = {"nouns": {"$elemMatch": {"name": value }}}
        # collection.find({'nouns': {"$elemMatch": {"name": "bakery"}}})
        # print(string)
        result = collection.find(string)
        for ptip in result:
            totalPtips.append(ptip)
            i += 1
            if(i == 10):
                break
        # return HttpResponse((value, collection.find_one()))
        return HttpResponse((value, totalPtips))

        # return HttpResponse(str(collection.find_one()))
    # return HttpResponse("Hello, world. You're at the polls index.")

# Establish a connection with mongo instance.
# conn = Connection(server,port)
# assert isinstance(user, mongoengine.django.auth.User)
