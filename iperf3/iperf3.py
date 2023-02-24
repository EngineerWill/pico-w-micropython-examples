import network
import time

ssid = 'A Network'
password = 'A Password'
#iperf3 server ip
host="192.168.1.2"

wlan = network.WLAN(network.STA_IF)

def connect_to_network():
    wlan.active(True)
    wlan.config(pm = 0xa11140) # Disable power-save mode
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])

connect_to_network()
# import upip
# upip.install("uiperf3")
import uiperf3
uiperf3.client(host,udp=True, reverse=False)