import time
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo


# Function to set servo angle
def set_angle(servo,angle):
    servo.angle = angle
    print(f'Servo angle:',angle)


def set_pulse_width(servo,pulse_width):
    """
    Set the pulse width directly.
    pulse_width should be between 500 and 2500 microseconds.
    """
    # Convert microseconds to fraction
    fraction = (pulse_width - 1000) / (2000 - 1000)
    servo.fraction = fraction

def test_position(angle=2):
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize PCA9685
    pca = PCA9685(i2c)

    # Set the PWM frequency
    pca.frequency = 40

    # Initialize servo on channel 1
    s = servo.Servo(
        pca.channels[1],
        min_pulse=1000,   # Typically 1000, we're extending lower
        max_pulse=2000   # Typically 2000, we're extending higher
    )
    # Example usage
    try:
        #while True:
            #set_angle(s,angle)    # Move to 0 degrees
            #time.sleep(3)
        set_angle(s,90)
        time.sleep(1)
        set_angle(s,80)
        time.sleep(1)
        set_angle(s,70)
        time.sleep(1)
        set_angle(s,60)
        time.sleep(1)
        set_angle(s,50)
        time.sleep(1)
        #set_angle(s,40)
        #time.sleep(1)
        #set_angle(s,50)
        #time.sleep(1)
        set_angle(s,60)
        time.sleep(1)
        set_angle(s,70)
        time.sleep(1)
        set_angle(s,80)
        time.sleep(1)
        set_angle(s,90)
        time.sleep(1)

    except KeyboardInterrupt:
        pca.deinit()
        print("Servo control stopped")

def test_PWM(pulse_width=100):
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize PCA9685
    pca = PCA9685(i2c)

    # Set the PWM frequency
    pca.frequency = 40

    # Initialize servo on channel 1
    s = servo.Servo(
        pca.channels[1],
        min_pulse=1000,   # Typically 1000, we're extending lower
        max_pulse=2000   # Typically 2000, we're extending higher
    )
    try:
        while True:
            # Move to extreme positions
            set_pulse_width(s,pulse_width)   # Minimum pulse width
            time.sleep(3)
            set_pulse_width(s,1500)
            time.sleep(3)

    except KeyboardInterrupt:
        pca.deinit()
        print("Servo control stopped")

if __name__ == "__main__":
    test_position(90)