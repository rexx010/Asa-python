def seconds_since_midnight(h, m, s):
 second_per_hour = 3600
 hour_in_seconds = h * second_per_hour
 minute_in_seconds = m * 60
 total = hour_in_seconds + minute_in_seconds + s

 return total


hour = 13
minutes = 30
second = 45
print('The number of seconds since midnight is ', seconds_since_midnight(hour, minutes, second))