import network
import asyncio
from mqtt_async import MQTTClient, config
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('wireless', '')
while not sta_if.isconnected():
    pass

config['server'] = '192.168.50.31'

client = MQTTClient(config, None)

async def foo():
    print(await client.connect())
    while True:
        await client.publish('topic', b'a' * 100, qos=0)


loop = asyncio.get_event_loop()
loop.run_until_complete(foo())

