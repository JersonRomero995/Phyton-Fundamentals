hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

convertomin = (int(hour*60)) + mins
totalmin = convertomin + dura
h = totalmin // 60
m = totalmin % 60

time1 = h % 24
time2 = m % 60
print(time1,":",time2)

#Just a small cosmetic thing if you want a cleaner output, right now it prints something like 13 : 16 with spaces around the colon. If you want it to look like 13:16 you can change your print to:
#python
print(time1, ":", time2, sep="")
#or using an f-string:
#python
print(f"{time1}:{time2}")


#course resolution

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')