Throbbing EDM Dance Light

This project is a step up from the typical blink example. It still pulses an LED, but rather than flashing on and off, it fades in and out gradually and can be timed to the beat of your favorite music.

How to use it...
1. Figure out the tempo of your music in beats per minute.
2. Open config.py in an editor like Thonny and set the value of BPM to the beats per minute you just measured.
3. Save the files to your ESP8266 nd reset it.

How it works...
Pulse width modulation (PWM) is used to create varying levels of brightness. Jarring transitions between on and off are smoothed out. Using a cosine wave to controll PWN, flashing becomes throbbing. Getting the throbbing to match the beat is a matter of converting BPM to milliseconds between beats. This process is described in the comments of main.py.

For an enhanced effect, connect two LEDs in parallel, but with their polarities reversed. Then, as one is fading in, the other is fading out.
