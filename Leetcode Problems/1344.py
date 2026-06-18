hours =  8
minute =  7
hour_constant = 1/12
hour_current =  (hours + (minute*hour_constant)/5)%12
hourAngle = hour_current*30
minuteAngle = minute*6
angle = abs(hourAngle - minuteAngle)
print(min(angle, abs(360-angle)))