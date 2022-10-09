# Throbbing EDM Dance Light
# A pulse-width modulated LED that fades in and out in sync with music.
from machine import Pin, PWM
from time import ticks_us, sleep_us
from math import pi, cos

GPIO = 2  # GPIO 2 is the built-in LED on a NodeMCU 8266. Change as needed.
led = PWM(Pin(GPIO), freq=1000)

bpm = 118  # Beats per minute (BPM) is the tempo of the music.
bps = bpm / 60  # Dividing BPM by 60 seconds/minute gives beats per second.
bpms = bps / 1000  # Dividing again by 1000 gives beats per millisecond.
period = 1 / bpms  # Period is the time between beats (expressed in milliseconds.) 

print("\n\n{:3d} BPM".format(bpm))

t = 0
while (1):
    start_time = ticks_us()
    a = cos(t) * 511 + 512  # Sine ranges from -1 to 1. PWM amplitude requires 0 to 1023.
    led.duty(int(a))  # LED brightness is controlled by duty cycle.
    t += pi / period  # Incrementing time by the beat period syncs the LED to every two beats.
    if (t > 2 * pi):  # 2pi radians is one full cycle of the sine wave.
        t = 0
    elapsed_time = ticks_us() - start_time
    sleep_us(1000 - elapsed_time)  # The loop delay is 1 millisecond, which is why beats per ms is important.