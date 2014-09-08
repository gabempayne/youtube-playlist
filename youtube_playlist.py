import random
import webbrowser
import time

# defines a variable as a text file
file_open = open("urls.txt", "r")
array = []
wait_time = 60  # wait time in seconds

# parses a file and appends each line to an array
for line in file_open:
	array.append(line)
file_open.close()  # closes file

# runs this function a certain amount of times
for i in range(10):
	time.sleep(wait_time)  # set wait time
	webbrowser.open(random.choice(array))



