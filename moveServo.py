from PCA9685 import PCA9685
import sys

def moveServo(channel, angle, pwm):
	# servo buzzes at angles 0-5 so change to 6 
	if(angle >= 0 and angle <= 5):
		angle = 6	
	
	pwmSignal = float(500+(angle)*(100/9)) 
	# 500  ==   0 degs
	# 1000 ==  45 degs
	# 1500 ==  90 degs
	# 2000 == 135 degs
	# 2500 == 180 degs
	# taken from wiki of servo controller
	pwm.setServoPulse(channel,pwmSignal)
	print('done')

if __name__=='__main__':
	try:
		channel = int(sys.argv[1])
		angle = float(sys.argv[2])
		if(angle > 180 or angle < 0):
			raise Exception('angle must be between 0-180')
		if(channel < 0 or channel > 15):
			raise Exception('channel must be between 0-15')

	except Exception as e:
		print(e)
		print("please provide channel (0-15) and angle (0-180)")
		print("Example python3 servoControl 4 90")
		sys.exit()
	else:
		pwm = PCA9685(0x40)
		pwm.setPWMFreq(50)
		print(channel)
		print(angle)
		moveServo(channel, angle, pwm)
