import paho.mqtt.client as mqtt
def on_connect(client,userdata,flags,rc):
    print("connected")
client=mqtt.Client()
client.will_set("Client","Disconnected",0,retain=False)
client.connect("192.168.75.97",1883,60)
client.on_connect=on_connect
client.publish("practice","Hello World")
# client.disconnect()
client.loop_forever()