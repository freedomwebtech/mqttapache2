from umqtt.simple import MQTTClient
from machine import Pin
pin=Pin(5,Pin.OUT)
pin.value(1)

def msg(a,b):
    data=(str(b,'utf-8'))
    print(data)
    if "status"in data:
        pin1=Pin(5,Pin.OUT)
        p=pin1.value()
        if p==1:
           m=str(p)
           server = "test.mosquitto.org"
           c = MQTTClient("esp8266",server)
           c.set_callback("test4")
           c.connect()
           c.publish("test4",'off')
           
        if p==0:
           server = "test.mosquitto.org"
           c = MQTTClient("esp8266",server)
           c.set_callback("test4")
           c.connect()
           c.publish("test4",'on')
    
           
    if "off" in data:
        pin.value(1)
    if "on" in data:
        pin.value(0)
        
        
        

        
    


def client():
    server="test.mosquitto.org"
    c = MQTTClient("umqtt_client", server)
    c.set_callback(msg)
    c.connect()
    c.subscribe("test2")
    c.wait_msg()
    c.check_msg()
    c.disconnect()
    
while True:
     client()
