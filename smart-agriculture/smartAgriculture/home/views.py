from django.shortcuts import render,HttpResponse
import json
from pymongo import database
from pymongo.message import _convert_write_result
import requests
import pymongo as mongo
from django.core.files.storage import FileSystemStorage
#import disease.ML


# Create your views here.

API_KEY="e10945655a16f4e6aceacf3158bd8952"
AGRO_API_KEY="1f8a0e19b649560f257d5009cb66258e"
default_polid="6044e4960573db290cc1c44b"

connection_string="mongodb+srv://admin:admin@cluster0.1rhlu.mongodb.net/"


dbclient=mongo.MongoClient(connection_string)
db=dbclient["AgrilData"]
col=db["allData"]

#Page routes
def home(response):
    return render(response,"overview.html")

def irrigation(response):
    return render(response,"irrigation.html")


def cropHealth(response):
    return render(response,"cropHealth.html")

def diseaseDetection(response):
    """
    if response.method == 'POST':
        uploaded_file = response.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        disease.ML.makecsv(uploaded_file.name)
        data,perc=disease.ML.test_image()
        result=str(data)+" with "+str("{:.2f}".format(perc))+" % assurance"
        return render(response,"disease.html", {'content':['Status: ',result]})
    """
    return render(response,"disease.html")

def weather(response):
    return render(response,"weather.html")

def login(response):
    return render(response,"login.html")

def signup(response):
    return render(response,'signup.html')

#API for current Weather 
def getWeatherAPI(response):
    if response.method == "POST":
        lat=response.POST['lat']
        lon=response.POST['lon']
        print(lat,lon)
        url = "http://api.openweathermap.org/data/2.5/weather?"
        data = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': "metric"
        }
        r = requests.get(url=url, params=data)
        context=json.dumps(r.json())
        return HttpResponse(context, content_type="application/json")
        
    return HttpResponse("{'status':'unknown'}", content_type="application/json")

def getAllWeatherAPI(response):
    if response.method == "POST":
        lat=response.POST['lat']
        lon=response.POST['lon']
        print(lat,lon)
        url = "http://api.openweathermap.org/data/2.5/onecall?"
        data = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': "metric"
        }
        r = requests.get(url=url, params=data)
        context=json.dumps(r.json())
        return HttpResponse(context, content_type="application/json")
        
    return HttpResponse("{'status':'unknown'}", content_type="application/json")

#API for historical NDVI data
def getNDVIAPI(response):
    if response.method=='POST':
        startDate=response.POST['startDate']
        endDate=response.POST['endDate']
        polygonId=response.POST['polid']
        print(startDate,endDate)
        url="http://api.agromonitoring.com/agro/1.0/ndvi/history?"
        data={
            'polyid':default_polid,
            'start':startDate,
            'end':endDate,
            'appid':AGRO_API_KEY
        }
        r=requests.get(url=url,params=data)
        context=json.dumps(r.json())
        return HttpResponse(context,content_type="application/json")
    return HttpResponse("{'status':'unknown'}",content_type='application/json')

def createNewUser(response):
    if response.method=='POST':
        fname=response.POST['fname']
        lname=response.POST['lname']
        username=response.POST['username']
        password=response.POST['password']
        email=response.POST['email']
        print(fname,lname,username,password,email)
        context={'status': 'success'}
        context=json.dumps(context)
        return HttpResponse(context,content_type='application/json')
    return HttpResponse(json.dumps("{'status': 'forbidden'}"),content_type='application/json')
    

def getIrrigationData(response):
    if response.method=='POST':
        dataList=[]
        sensor=response.POST['sensor']
        sensor='node1/'+sensor
        print(sensor)
        for item in col.find({"sensor" : sensor},{'_id' : 0}):
            dataList.append(item)
        print(dataList)
        context={"data" : dataList}
        print(context)
        return HttpResponse(json.dumps(context),content_type='application/json')

    return HttpResponse(json.dumps("{'status': 'forbidden'}"),content_type='application/json')
