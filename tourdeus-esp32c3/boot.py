# You should not need to edit this file. Use settings in config.py instead.
from machine import Pin
from config import AP_NAME, AP_PASS, WIFI_TIMEOUT, WEBREPL_PASS
from network import WLAN, AUTH_WPA2_PSK, STA_IF
from time import ticks_ms
from webrepl import start

print('Starting in wifi station mode...')
wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(AP_NAME, AP_PASS)
start_time = ticks_ms()
while not wlan.isconnected():
    if (ticks_ms() - start_time > WIFI_TIMEOUT * 1000):
        break
if (wlan.isconnected()):
    oled.text(f'{wlan.ifconfig()[0]}', 0, 56)
    start(password=WEBREPL_PASS)
