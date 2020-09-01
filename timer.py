import time

for hour in range (0,100):
	for minute in range (0,600):
		for second in range (0,600):
			print("{}:{}:{}". format(hour,minute,second))
			time.sleep(0.00000000000000000000000000000000001)