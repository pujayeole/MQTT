import paho.mqtt.client as mqtt
def on_connect(client,userdata,flags,rc):
    print("connected")
client=mqtt.Client()
client.connect("192.168.75.97",1883,60)
client.on_connect=on_connect
file=open("/proc/loadavg","r")
while(1):
        for line in file:
            fields=line.split(" ")
            first = fields[0]
            second = fields[1]
            third = fields[2]
        print(first+"first"+" "+second+"second"+" "+third+"third"+" ")
        print("connected")
client=mqtt.Client()
client.connect("192.168.75.97",1883,60)
client.on_connect=on_connect
client.publish("/pc/load/1minavg","hello")
client.publish("/pc/load/5minavg","hello")
client.publish("/pc/load/10minavg","hello")
client.loop_forever()
file.close()
