import sys
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

# ------------------------------------
# set or reset all pins of user give ON/OFF params
if len(sys.argv) > 1:
    if "on" == sys.argv[1].lower():
        for p in pins:
            p.value = True
        sleep(30)
        exit()
    elif "off" == sys.argv[1].lower():
        for p in pins:
            p.value = False
        exit()
    elif "test" == sys.argv[1].lower():
        for p in pins:
            p.value = True
            sleep(2)
        for p in pins:
            p.value = False
            sleep(2)
        exit()
# ------------------------------------

pattern_algorithm = PatternAlgorithm(18)

cur_state = PatternAlgorithm.inverse_initial_state()

sleep_time = 0.08  # in seconds

while True:
    new_state = pattern_algorithm.next()

    for idx, new_pin_value in enumerate(new_state):
        if cur_state[idx] != new_pin_value:
            pins[idx].value = (new_pin_value == 1)

    cur_state = new_state
    sleep(sleep_time)
