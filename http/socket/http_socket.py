# Connect to network
import network
import time
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
# Should be connected and have an IP address
wlan.status() # 3 == success
wlan.ifconfig()

# Get IP address for google.com
import socket
ai = socket.getaddrinfo("raspberrypi.com", 80)
addr = ai[0][-1]

# Create a socket and make a HTTP request
s = socket.socket()
s.connect(addr)
s.send(b"GET / HTTP/1.0\r\n\r\n")

# Print the response
print(s.recv(512))
