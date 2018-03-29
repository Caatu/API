#!/usr/bin/python3
import paho.mqtt.client as  mqtt
import json, time

def on_connect(client, userdata, flags, rc):
    """
        Callback funcition to control the network loop
        Values to rc:
            0: Connection successful
            1: Connection refused – incorrect protocol version
            2: Connection refused – invalid client identifier
            3: Connection refused – server unavailable
            4: Connection refused – bad username or password
            5: Connection refused – not authorised
    """
    if(rc == 0):
        client.connected_flag = True
        print("Connection OK")
    else:
        client.bad_connection_flag = True
        print("Bad connection Returned code=",rc)


def on_message(client, userdata, message):
    print("Message received " ,str(message.payload.decode("utf-8")))
    print("Message qos=",message.qos)
    print("Message retain flag=",message.retain)

def initializeConnection(username, password, client_id, broker, port):
    """
        Create client object and initialize the connection with mqtt server
        More about client object:
            http://www.steves-internet-guide.com/client-objects-python-mqtt/
    """
    global client
    mqtt.Client.connected_flag = False # Control Tag (Network loop)
    mqtt.Client.bad_connection_flag = False

    client = mqtt.Client(
        client_id=client_id, 
        clean_session=False,  
    )
    client.on_connect   =   on_connect
    client.on_message   =   on_message
    client.username_pw_set(username=username, password=password)
    print("Connecting to broker")
    try:
        client.connect(broker,port=port)
    except:
        print("Connection failed")
        client.bad_connection_flag = True
    client.loop_start()
    # Wait to connection success or error occur
    while not client.connected_flag and not client.bad_connection_flag:
        print("In wait loop")
        time.sleep(1)
    if client.bad_connection_flag:
        # When occur error in connection stop the program
        # TODO: Filter possibles errors in on_conect and print this on log file
        finish()
    print("In Main Loop")

def finish():
    """
        Finish the loop of callbacks from paho-mqtt and exit the program
    """
    client.disconnect()
    client.loop_stop()

brokerUserName = "gustavoguerino2@gmail.com"
brokerPassword = "66db79f5"
brokerApi = "mqtt.dioty.co"
brokerPort = 1883

initializeConnection(brokerUserName, brokerPassword, "samsung-albert", brokerApi, brokerPort)

client.subscribe("/gustavoguerino2@gmail.com/MAUROVIADO")