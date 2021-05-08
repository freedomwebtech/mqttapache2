import paho.mqtt.client as mqtt
import time

     
def on():
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("on",'utf-8')))     


      

on()
