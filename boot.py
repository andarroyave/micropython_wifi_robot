import machine
import network

if machine.reset_cause() != machine.SOFT_RESET:
    wlan = network.WLAN(network.STA_IF)
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    if not wlan.active():
        wlan.active(True)
    wlan.ifconfig(('192.168.0.18', '255.255.255.0', '192.168.0.1', '8.8.8.8'))    
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Jorge A', '820321880607')
        while not wlan.isconnected():
            pass
print('network config:', wlan.ifconfig())
