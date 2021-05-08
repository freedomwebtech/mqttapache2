import paho.mqtt.client as mqtt
import time





def off():
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("raspberry pi 400")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("off",'utf-8')))
    
off()    