# On 8266, shutdown access point, which is active by default.
from network import WLAN, AP_IF
ap_if = WLAN(AP_IF)
ap_if.active(False)
