# You should not need to edit this file. Use settings in config.py instead.
from config import AP_NAME, AP_PASS, WIFI_TIMEOUT, WEBREPL_PASS
from machine import Pin
from network import WLAN, STA_IF
from time import ticks_ms, ticks_diff
from webrepl import start

p12 = Pin(12, Pin.OUT)  # labeled as D4
p13 = Pin(13, Pin.OUT)  # labeled as D5

p12.value(1)
p13.value(1)

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
    p13.value(0)
    start(password=WEBREPL_PASS)
    p12.value(0)
