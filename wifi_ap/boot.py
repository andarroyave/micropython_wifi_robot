import network

server = network.WLAN(network.AP_IF)
server.active(True)
server.config(essid='JA_CAR',password='12345678')
