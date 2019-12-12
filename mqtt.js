var mqtt = require('mqtt')
var client = mqtt.connect('mqtt://192.168.75.97')
client.on('connect', function () {
    console.log("connect")
client.subscribe('presence')
   client.publish('presence', 'Hello')

})
client.on('message', function (topic, message) {
    // message is Buffer
    console.log(message.toString())
    client.end()
})