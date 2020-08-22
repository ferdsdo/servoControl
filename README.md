# servoControl
Servo Controller code for raspberry pi servo controller HAT

Uses HAT servo controller by waveshare
https://www.waveshare.com/wiki/Servo_Driver_HAT

# How to use
call the code in the terminal
Example:
  `python3 moveServo.py 0 90`
   0 is the channel of the servo
   90 is the angle the servo will stop at
   **Note:** angles are between 0-180 (inclusive) and channels are between 0-15 (inclusive)
