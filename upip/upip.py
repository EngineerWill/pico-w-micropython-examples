import time
import network

ssid = 'A Network'
password = 'A Password'

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
        print('/****************ifconfig****************/')
        print('IP address   =   ' + status[0])
        print('Subnet Mask  =   ' + status[1])
        print('Gateway      =   ' + status[2])
        print('DNS server   =   ' + status[3])
        print('/****************************************/')

connect_to_network()

import upip
upip.install("micropython-pystone_lowmem")
import pystone_lowmem
pystone_lowmem.main()
