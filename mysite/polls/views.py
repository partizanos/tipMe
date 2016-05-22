from django.http import HttpResponse
from pymongo import MongoClient
from django.template import loader


import json
from bson import ObjectId


c = MongoClient()
db = c.yelp


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def index(request):
    template = loader.get_template("polls/generic.html")
    return HttpResponse(template.render())


def db_req(request):
    json_data = {}

    if request.method == 'GET':

        collection = db['ptip']
        value = request.GET.get('value').encode('utf8')
        i = 0
        string = {"nouns": {"$elemMatch": {"name": value}}}
        result = collection.find(string)

        for ptip in result:
            name_query = {"business_id": ptip['bus_id']}
            try:
                label = db.business.find(name_query)[0]['name']
                json_data[label] = ptip
                i += 1
                if (i > 20):
                    break
            except:
                pass

        return HttpResponse(JSONEncoder().encode(json_data))


def bus_search(request):
    json_data = []

    if request.method == 'GET':
        # c = MongoClient()
        # db = c.yelp

        value = request.GET.get('value').encode('utf8')
        name_query = {"name": value}

        # bus_id = db.businessOld.find(name_query)[0]['business_id'].encode('utf8')
        bus_id_list = db.businessOld.find(name_query)
        for bus_id in bus_id_list:
            bus_name=bus_id['business_id'].encode('utf8')
            print(bus_name)
            tips_query = {"bus_id": bus_name}
            # while resulr
            result = db['ptip'].find(tips_query)
            # print(result)

            for ptip in result:
                json_data.append(ptip)

        return HttpResponse(JSONEncoder().encode(json_data))
