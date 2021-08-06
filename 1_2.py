second = int(input('Введите количество секунд - '))
hour = second//3600
hourprint = hour%24
minute = second//60
minuteprint = minute%60
end = second%60

print("{:02d}".format(hourprint),':',"{:02d}".format(minuteprint),':',"{:02d}".format(end))
#print(hour+minute)
