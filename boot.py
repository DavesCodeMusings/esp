# Boot ESP32 wifi as access point or station and display connect info on OLED.
# For Wemos LOLIN32 with built-in SSD1306 OLED (and clones.)
# You should not need to edit this file. Use settings in config.py instead.
from machine import Pin, SoftI2C, Timer
from ssd1306 import SSD1306_I2C
from config import IS_ACCESS_POINT, AP_NAME, AP_PASS, WIFI_TIMEOUT, WEBREPL_PASS, SCREEN_TIMEOUT
from network import WLAN, AUTH_WPA2_PSK, AP_IF, STA_IF
from time import ticks_ms
from webrepl import start

# Configure built-in OLED
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))  # Wemos board uses pins 4 (clock) & 5 (data)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# Setup screen saver using BOOT button repurposed to trigger a wake up
def blank_screen(screen_timer):
    oled.poweroff()

def wake_screen(pin):
    screen_saver.deinit()  # Cancel (possibly) running timer
    oled.poweron()
    screen_saver.init(period=SCREEN_TIMEOUT*1000, mode=Timer.ONE_SHOT, callback=blank_screen)

screen_saver = Timer(0)
screen_saver.init(period=SCREEN_TIMEOUT*1000, mode=Timer.ONE_SHOT, callback=blank_screen)
boot_button = Pin(0, Pin.IN, Pin.PULL_UP)
boot_button.irq(trigger=Pin.IRQ_FALLING, handler=wake_screen)

# Start wifi networking showing status on OLED
wlan = None
if (IS_ACCESS_POINT):
    print('Starting in wifi access point mode...')
    wlan = WLAN(AP_IF)
    wlan.config(authmode=AUTH_WPA2_PSK, essid=AP_NAME, password=AP_PASS)
    wlan.active(True)
    while (wlan.active() == False):
        pass
    print(f'SSID: {AP_NAME}')
    print(f'Password: {AP_PASS}')
    oled.text('Access Point', 0, 0)
    oled.text('SSID:', 0, 16)
    oled.text(f'{AP_NAME}', 0, 28)
    oled.text('Password:', 0, 44)
    oled.text(f'{AP_PASS}', 0, 56)
    oled.show()
    print(f'{wlan.ifconfig()}')
else:
    print('Starting in wifi station mode...')
    oled.text('Wifi client', 0, 0)
    oled.text('SSID:', 0, 16)
    oled.text(f'{AP_NAME}', 0, 28)
    oled.text('Connection...', 0, 44)
    oled.show()
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
    else:
        oled.text('Timed out.', 0, 56)        
    oled.show()
