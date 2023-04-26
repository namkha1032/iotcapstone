import sys
from Adafruit_IO import MQTTClient
import random
import time

AIO_FEED_ID = "iot.sensor-humid"
AIO_FEED_ID2 = "iot.sensor-temp"
AIO_FEED_ID3 = "iot.sensor-light"
AIO_FEED_ID3 = "iot.sensor-ir"
AIO_FEED_ID4 = "iot.device-led"
AIO_FEED_ID5 = "iot.device-fan"

AIO_USERNAME = "nguyennamkha"
AIO_KEY = "aio_JqXH23OJnNUDKtqXYIg8AG1vfWd3"
def connected(client):
    print ("Connect successfully...")
    client.subscribe(AIO_FEED_ID)
    client.subscribe(AIO_FEED_ID2)
    client.subscribe(AIO_FEED_ID3)
    client.subscribe(AIO_FEED_ID4)
    client.subscribe(AIO_FEED_ID5)

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
    measuredTemp = random.randint(0, 40)
    print ("Measured temperature is :", measuredTemp )
    client.publish("iot.sensor-temp", measuredTemp)

    # deviceFan = 0
    # if measuredTemp in range(0,11):
    #     deviceFan = 0
    # if measuredTemp in range(11,21):
    #     deviceFan = 1
    # if measuredTemp in range(21,31):
    #     deviceFan = 2
    # if measuredTemp in range(31,41):
    #     deviceFan = 3
    # client.publish("iot.device-fan", deviceFan)

    measuredHumid = random.randint(0, 100)
    print ("Measured humidity is :", measuredHumid )
    client.publish("iot.sensor-humid", measuredHumid)
    
    measuredLight = random.randint(0, 100)
    print ("Measured light is :", measuredLight )
    client.publish("iot.sensor-light", measuredLight)
    
    # measuredIR = random.randint(0, 1)
    # print ("Measured IR is :", measuredIR )
    # client.publish("iot.sensor-ir", measuredIR)
    # deviceLED = 1
    # if measuredIR == 1:
    #     deviceLED = 0
    # print ("Device LED is :", deviceLED )
    # client.publish("iot.device-led", deviceLED)
    time.sleep(10)