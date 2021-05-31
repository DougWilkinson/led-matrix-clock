import dht
from machine import PWM,ADC,Pin,Timer,reset,reset_cause
import time
from blink import blink
import json
from umqtt.simple import MQTTClient
import network
from gc import mem_free
from publish import publish

class Sensor:

    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    clock = time.time
    lastblink = time.time()
    CallBlink = blink
    Callmemfree = mem_free
    Callpublish = publish
    mqttclient = MQTTClient
    name = ""
    basetopic = ""
    usingmqtt = False
    mqttconnected = False
    publishing = False
    lastmqttretry = time.time() - 15 
    
 