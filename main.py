import sys
from Adafruit_IO import MQTTClient
import random
import time

AIO_FEED_ID = "iot.light"
AIO_FEED_ID2 = "iot.fan"
AIO_USERNAME = "nguyennamkha"
AIO_KEY = "aio_uHZr29Iu1U1aVqVbWJWeSuSEvOmz"

def connected(client):
    print ("Connect successfully...")
    client.subscribe(AIO_FEED_ID)
    client.subscribe(AIO_FEED_ID2)

def subscribe(client,userdata,mid,granted_qos):
    print("Subcribe successfully...")

def disconnected(client):
    print ("Disconnect...")
    sys.exit (1)

def message(client,feed_id,payload):
    print("Receive value: " + payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    measuredTemp = random.randint (0 , 50)
    print ("Measured temperature is :", measuredTemp )
    client.publish("iot.temp", measuredTemp)
    
    measuredHumid = random.randint (0 , 100)
    print ("Measured humidity is :", measuredHumid )
    client.publish("iot.humidity", measuredHumid)
    time.sleep(5)