import RPi.GPIO as GPIO
import time
'''

LED_PIN = 13  # Replace with your GPIO pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
'''

# Replace with your actual pin number
PIN_TO_TEST = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TO_TEST, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print(f"Testing GPIO pin {PIN_TO_TEST}. Press Ctrl+C to exit.")
    while True:
        state = GPIO.input(PIN_TO_TEST)
        print(f"Pin {PIN_TO_TEST} state: {'HIGH' if state else 'LOW'}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Test ended by user")
finally:
    GPIO.cleanup()