import os, time, brickpi3

# Initialize the EV3 Brick
BP = brickpi3.BrickPi3()

# Initialize EV3 touch sensor and motors
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
touchButton = 0

# Without a delay reading sensor data can cause an error
time.sleep(0.5)

# Quite loop when CTRL+C is pressed
try:

    # Create a loop to react to buttons
    while True:

        # Get touch sensor status
        touchButton = BP.get_sensor(BP.PORT_1)
            
        # If the touch sensor is pressed
        if touchButton:

            BP.set_motor_power(BP.PORT_A, 100)

            # Turn off BrickPi on board LED
            BP.set_led(1) 

            # Turn on Raspberry Pi on board LED
            os.system('echo 1 | sudo dd status=none of=/sys/class/leds/led0/brightness') 
        
        # If the touch sensor is released
        else:

            BP.set_motor_power(BP.PORT_A, 0)

            # Turn off BrickPi on board LED
            BP.set_led(0)

            # Turn off Raspberry Pi on board LED
            os.system('echo 0 | sudo dd status=none of=/sys/class/leds/led0/brightness')

        # Loop delay
        time.sleep(0.1)

# Result of CTRL+C
except KeyboardInterrupt:
    
    # Unconfigure the sensors
    BP.reset_all() 