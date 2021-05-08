import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print (str(message.payload.decode("utf-8")))
def sub():
    mqttBroker ="test.mosquitto.org"

    client = mqtt.Client("raspberry pi 4")
    client.connect(mqttBroker) 

    client.loop_start()


    client.subscribe("test4")
    client.on_message=on_message 
    time.sleep(1)
    client.loop_stop()

def status():
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("status",'utf-8')))     

status()
sub()
