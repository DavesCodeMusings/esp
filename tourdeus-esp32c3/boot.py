from config import AP_NAME, AP_PASS, WIFI_TIMEOUT
from machine import Pin
from network import WLAN, STA_IF
from time import ticks_ms, ticks_diff

D4 = Pin(12, Pin.OUT)  # labeled as D4
D5 = Pin(13, Pin.OUT)  # labeled as D5

D4.value(0)
D5.value(1)

wlan = WLAN(STA_IF)
wlan.active(True)
print(f'\nConnecting to {AP_NAME}...')
if not wlan.isconnected():
    start_time = ticks_ms()
    wlan.connect(AP_NAME, AP_PASS)
    while not wlan.isconnected():
        if ticks_diff(ticks_ms(), start_time) > WIFI_TIMEOUT * 1000:
            print('Connection timeout.')
            break

if wlan.isconnected():
    print(wlan.ifconfig()[0])
    D5.value(0)
