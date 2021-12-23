from flask import request
from flaskr.app import app

import json
import requests
import traceback

from Comfortable_temperature_AI.src.TemperatureDetermination import TemperatureDetermination
from Home_appliance_control_AI.applianceControl import control
from flaskr.databases.collection_models.temperature import Temperature
from flaskr.util.temperatureCategory import TemperatureCategory

#リモコンアプリからの温度感覚
@app.route("/temperatureCurrent", methods=["GET"])
def get_tCurrent():
    try:
        
        #各カテゴリの最新データ
        tCurrent_A = Temperature.objects(temperatureCategory= TemperatureCategory.tActual).order_by("-time").first() 
        tCurrent_I = Temperature.objects(temperatureCategory= TemperatureCategory.InsideTemp).order_by("-time").first()
        tCurrent_O = Temperature.objects(temperatureCategory= TemperatureCategory.OutsideTemp).order_by("-time").first()
        tCurrent_S = Temperature.objects(temperatureCategory= TemperatureCategory.tSuitable).order_by("-time").first()
        

        print({"status":"200 OK","tCurrent":{
            "InsideTemp":tCurrent_I.Temperature if tCurrent_I != None else None, 
            "OutsideTemp":tCurrent_O.Temperature if tCurrent_O != None else None, 
            "tActual":tCurrent_A.Temperature if tCurrent_A != None else None, 
            "tSuitable":tCurrent_S.Temperature if tCurrent_S != None else None
            }})
        
        return {"status":"200 OK","tCurrent":{
            "InsideTemp":tCurrent_I.Temperature if tCurrent_I != None else None, 
            "OutsideTemp":tCurrent_O.Temperature if tCurrent_O != None else None, 
            "tActual":tCurrent_A.Temperature if tCurrent_A != None else None, 
            "tSuitable":tCurrent_S.Temperature if tCurrent_S != None else None
            }}
    except Exception as e:
        traceback.print_exc()
        return {"status":"400 Bad Request"}