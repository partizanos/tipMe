# from django.shortcuts import render
from django.http import HttpResponse
# import mongoengine
from pymongo import MongoClient
from django.template import loader


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# JSONEncoder().encode(analytics)

def index(request):
    # server = "localhost"
    # port = 27017
    # c = MongoClient()
    # db = c.yelp
    # collection = db['tip']

    template = loader.get_template("polls/generic.html")
    return HttpResponse(template.render())


def db_req(request):
    json_data = {}
    # json_data = json.dumps({})
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
        string = {"nouns": {"$elemMatch": {"name": value}}}
        # collection.find({'nouns': {"$elemMatch": {"name": "bakery"}}})
        # print(string)
        result = collection.find(string)
        for ptip in result:
            name_query = {"business_id": ptip['bus_id']}
            label = db.business.find(name_query)[0]['name']
            # totalPtips.append(ptip)
            json_data[label] = ptip
            # json_data[label.encode('utf8')] = ptip.encode('utf8')
            # totalPtips.append([label, ptip])
            i += 1
            if(i == 10):
                break
        # return HttpResponse((value, collection.find_one()))

        return HttpResponse(JSONEncoder().encode(json_data))

        # return HttpResponse(str(collection.find_one()))
    # return HttpResponse("Hello, world. You're at the polls index.")

# Establish a connection with mongo instance.
# conn = Connection(server,port)
# assert isinstance(user, mongoengine.django.auth.User)
