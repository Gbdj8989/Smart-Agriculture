import paho.mqtt.client as mqtt
import pymongo as mongo
from datetime import datetime


#constants
broker_address="192.168.0.58"
port=1880
connection_string="mongodb://192.168.0.58:1990/"


dbclient=mongo.MongoClient(connection_string)   
db=dbclient["AgrilData"]
col=db["allData"]


def connect_status(rc):
    if rc==0 : 
        return "CONNECTION_SUCCESSFULL"
    elif rc==1 :
        return "Connection refused - incorrect protocol version"
    elif rc==2 :
        return "Connection refused - invalid client identifier"
    elif rc==3 :
        return "Connection refused - server unavailable"
    elif rc==4 :
        return "Connection refused - bad username or password"
    elif rc==5 :
        return "Connection refused - not authorised"
    else:
        return "CONNECTION_UNSUCCESSFULL"


def on_connect(client,userdata,flags,rc):
    print("Status: "+connect_status(rc))
    client.subscribe("node1/soilMoisture")
    client.subscribe("node1/temperature")
    client.subscribe("node1/humidity")

def on_message(client,userdata,msg):
    now= datetime.now()
    print("Message ["+msg.topic+"] : "+str(msg.payload))
    new_dict={"sensor": msg.topic , "data" : msg.payload, "timestamp" : now}
    col.insert_one(new_dict)

client=mqtt.Client("IOT-LAB_PI_DB")
client.connect(broker_address,port) 
client.on_connect=on_connect
client.on_message=on_message
client.loop_forever()

