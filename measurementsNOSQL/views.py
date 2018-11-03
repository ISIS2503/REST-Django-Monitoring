from django.shortcuts import render
from rest_framework import (response, schemas, filters, generics, viewsets,
                            views)
from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from django.conf import settings
from bson import Binary
from bson.json_util import dumps
import time


# Create your views here.

@api_view(["GET","POST"])
def measurementList(request):
    result = []
    if request.method == "GET":
        client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
        db = client[settings.MONGO_DB]
        db.authenticate( settings.MLAB_USER, settings.MLAB_PASSWORD)
        measurements = db["variableSinPatrones"]
        data = measurements.find({})
        # for dto in data:
        #     json_data = {

        #        # "_id": dto["_id"],                
        #         "elId": dto["elId"],
        #         "measurement" : dto["measurement"],
        #         "value" : dto["value"],
        #         "unit" : dto["unit"],
        #         "place" : dto["place"],
        #         "time" : dto["time"]
                
        #     }
        #     result.append(dumps(data))
        client.close()
        return JsonResponse(dumps(data).replace("\'", '"'), safe=False)
    
    elif request.method == "POST":
        client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
        db = client[settings.MONGO_DB]
        db.authenticate( settings.MLAB_USER, settings.MLAB_PASSWORD)
        db = client[settings.MONGO_DB]
        measurements = db["variableSinPatrones"]
        data = JSONParser().parse(request)
        
        
        idData = int((time.time()*1000) % 86400000)
        data["elId"] = idData
        nombreAtributo = "measurement_"+data["place"]
        # datoAgregar = {
        #     nombreAtributo : data["value"]
        # }
        # result = measurements.findOneAndUpdate(
        #     {"variable": data["measurement"]},
        #     {"$set": {nombreAtributo: data["value"]}}
        # )
        result = measurements.find({})
        respo = {
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)
    
    

@api_view(["PUT", "GET", "DELETE"])
def measurementDetail(request, pk, format=None):
    if request.method == "GET":
        result = []
        client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
        db = client[settings.MONGO_DB]
        db.authenticate( settings.MLAB_USER, settings.MLAB_PASSWORD)
        db = client[settings.MONGO_DB]
        measurements = db["measurements"]
        data = measurements.find({"id": pk})
        print(data)
        for dto in data:
            jsonData = {
               # "_id": dto["_id"],
                "measurement" : dto["measurement"],
                "value" : dto["value"],
                "unit" : dto["unit"],
                "place" : dto["place"],
                "time" : dto["time"],
                "elId": dto["elId"]
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    elif request.method == "DELETE":
        client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
        db = client[settings.MONGO_DB]
        db.authenticate( settings.MLAB_USER, settings.MLAB_PASSWORD)
        db = client[settings.MONGO_DB]
        measurements = db["measurements"]
        result = measurements.remove({"_id": MongoObjectID(str(pk))})
        respo = {
            "MongoObjectID": str(result),
            "Message": "Objeto eliminado"
        }
        client.close()
        return JsonResponse(respo, safe = False)        






    
        

