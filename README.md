# What is it?

The Wemos LOLIN32 with OLED is a ESP32 microcontroller with an integrated 128x64 OLED display driven by an SSD1306. All of this is well supported by MicroPython. The code in this repository is specifically written to take advantage of the LOLIN32 with OLED and clone boards.

boot.py -- start wifi networking and display status on the OLED

* Connect to an existing access point in station mode or use ESP32 itself as an access point. (Mode is configurable using config.py.)
* Display SSID and password on OLED for AP mode or SSID and IP address in station mode.
* Start WebREPL (when in station mode) to allow connection to MicroPython without USB.
* Both station and AP modes feature automatic screen blanking to avoid OLED burn-in. Pressing BOOT button re-activates the display.

config.py -- configurable parameters used by boot.py

* AP_NAME
* AP_PASS
* IS_ACCESS_POINT
* WIFI_TIMEOUT
* WEBREPL_PASS
* SCREEN_TIMEOUT

IS_ACCESS_POINT is a True/False boolean. Timeouts are expressed in units of seconds. WEBREPL_PASS must be 4 to 9 characters.

# Why?

boot.py was created with the idea of having one program to load on multiple ESP32 devices that could then be configured as one access point and several clients. The only requirement is to set the config.py parameter `IS_ACCESS_POINT = True` on the one device serving as the AP.
