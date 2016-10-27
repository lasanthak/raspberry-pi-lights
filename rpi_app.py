from gpiozero import OutputDevice
from time import sleep
from pin_patterns import PatternAlgorithm

pins = [
    OutputDevice(pin=21, active_high=False),
    OutputDevice(pin=20, active_high=False),
    OutputDevice(pin=16, active_high=False),
    OutputDevice(pin=12, active_high=False),
    OutputDevice(pin=7, active_high=False),
    OutputDevice(pin=8, active_high=False),
    OutputDevice(pin=25, active_high=False),
    OutputDevice(pin=24, active_high=False)
]

pattern_algorithm = PatternAlgorithm()

cur_state = PatternAlgorithm.inverse_initial_state()

sleep_time = 0.3  # in seconds

while True:
    new_state = pattern_algorithm.next()

    for idx, new_pin_value in enumerate(new_state):
        if cur_state[idx] != new_pin_value:
            pins[idx].value = (new_pin_value == 1)
    sleep(sleep_time)
