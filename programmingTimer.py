
import time, os, datetime

def timerRun(programRunning, mins, dir, exportFile, completeDir):
    print("Timer started")
    print("Press Ctrl-C to exit")
    while(programRunning):
        try:
            time.sleep(60) # sleeps for 1 minute
            mins += 1 # so after 1 minute has passed,
            # add it to mins variable
            print(str(mins) + " " + " minute(s)," + " " + str(((mins*60)/3600)) + " hour(s)")

        except KeyboardInterrupt:
            exportTime(mins, dir, exportFile, completeDir)
            programRunning = False

def exportTime(mins, dir, exportFile, completeDir):
	if(dir != ''):
		if(os.path.exists(dir) == False):
		    os.makedirs(dir)
		
		file = open(completeDir, 'a')
		file.write("<" + getDateTime() + ">" + " " + str(mins) + " " + " minute(s)," + " " + str(((mins*60)/3600)) + " hour(s)\n")
		file.close()
		print("Time successfully exported to %s" % completeDir)
		
	else:
		print("Could not export, directory input is empty")

def getDateTime():
    now = datetime.datetime.now()
    hour = now.hour
    min = now.minute
    date = datetime.date.today()

    if(hour > 12):
        return("%s %s:%s PM" % (date, hour-12, min))

    elif(hour < 12):
        return("%s %s:%s AM" % (date, hour, min))
    
    elif(hour == 0):
        return("%s 12:%s" % (date, min))

    else:
        return("%s 12:%s AM" % (date, min))


programRunning = True
mins = 0
dir = input("Enter a directory to save results: ")
exportFile = r"programmingTimes.txt"
completeDir = os.path.join(dir, exportFile)

timerRun(programRunning, mins, dir, exportFile, completeDir)
