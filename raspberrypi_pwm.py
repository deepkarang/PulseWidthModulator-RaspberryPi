import pigpio
import time

pi = pigpio.pi()

#target GPIO pin on Raspberry Pi
servo = 18

#speed
slow = 1
fast = 20
speed = fast

#motor rotation endpoints
#10000 corresponds to 1% duty cycle
start_rotation = 25000
end_rotation = 125000

#target PWM signal frequency in Hz
targ_pwm_freq = 50


try:
	#begin PWM signal generation
	while True:	
		t0 = time.time()
		for duty_cycle in range(start_rotation, end_rotation, speed):
			pi.hardware_PWM(servo, targ_pwm_freq, duty_cycle)
		for duty_cycle in range(end_rotation, start_rotation, -1*speed):
			pi.hardware_PWM(servo, targ_pwm_freq, duty_cycle)
		print("Total time for revolution" + str(time.time()-t0))
except KeyboardInterrupt:
	#end PWM signal generation
	pi.hardware_PWM(0,0,0)

