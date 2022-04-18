
class time :
    hour = 0
    minute = 0
    dayRollOver = 0
    day = None

    def __init__(self,time,day=None) :
        # split time by assuming that we are receiving an item in the format of "[hours]:[minutes] [period]"
        period = strSplit(time," ")[1] # grab just the period
        hourMinute = strSplit(strSplit(time," ")[0],":")

        self.hour =  int(hourMinute[0])
        self.minute =  int(hourMinute[1])
        self.day = day

        if period == "PM" :
            self.addHours(12)

    def addHours(self,numHours) :
        # find new hour count
        newHours = self.hour + numHours
        # count down the days that may have been added
        rollOver = 0
        if newHours > 23 :
            while newHours > 23 :
                newHours -= 24
                rollOver += 1
        # update values
        self.hour = newHours
        self.dayRollOver += rollOver
        
    def addMinutes(self,numMinutes) :
        # find new hour count
        newMinutes = self.minute + numMinutes
        # count down the days that may have been added
        rollOver = 0
        if newMinutes > 60 :
            while newMinutes > 60 :
                newMinutes -= 60
                rollOver += 1
        # update values
        self.minute = newMinutes
        self.addHours(numHours=rollOver)

    # assume that the day is not "None"
    def getDayName(self,dayNum) : 
        if dayNum == 1 :
            return "Sunday"
        elif dayNum == 2 :
            return "Monday"
        elif dayNum == 3 :
            return "Tuesday"
        elif dayNum == 4 :
            return "Wednesday"
        elif dayNum == 5 :
            return "Thursday"
        elif dayNum == 6 :
            return "Friday"
        elif dayNum == 7 :
            return "Saturday"
        else :
            return "N/A"

    def getDayNum(self,dayName) :
        if dayName.lower() == "sunday" :
            return 1
        elif dayName.lower() == "monday" :
            return 2
        elif dayName.lower() == "tuesday" :
            return 3
        elif dayName.lower() == "wednesday" :
            return 4
        elif dayName.lower() == "thursday" :
            return 5
        elif dayName.lower() == "friday" :
            return 6
        elif dayName.lower() == "saturday" :
            return 7
        else :
            return 0

    def getFormattedTime(self) : 
        fPeriod = "AM"
        fHour = self.hour
        fMinute = self.minute
        minutePad = ""
        fDayTag = ""

        # add padding to the minute value if required to maintain a constant two digit format
        if fMinute < 10 :
            minutePad = "0"
        # convert out of military time
        if fHour > 12 and fHour < 24 :
            fHour = fHour - 12
            fPeriod = "PM"
        elif fHour == 12 :
            fPeriod = "PM"
        elif fHour == 24 :
            fHour = fHour - 12 #just subtract, keep it am
        elif fHour == 0 :
            fHour = 12 
        # if a day is specified then add ", [Day Name]" to the output
        if self.day != None : 
            dayNum = self.getDayNum(dayName=self.day) + self.dayRollOver
            if dayNum > 7 :
                while dayNum > 7 :
                    dayNum -= 7
            fDayTag = f", {self.getDayName(dayNum=dayNum)}"
        # it the clock rolls-over then add " (next day)" after the time
        if self.dayRollOver == 1 : 
            fDayTag = f"{fDayTag} (next day)"
        # if the clock rolls-over multiple times then add " ([x] days later)" after the time
        elif self.dayRollOver > 1 :
            fDayTag = f"{fDayTag} ({self.dayRollOver} days later)"

        return f"{fHour}:{minutePad}{fMinute} {fPeriod}{fDayTag}"

# split a string into a list where the specified character appears
def strSplit(toSplit="",delimiter=",") : 
    splitList = []
    prevPos = 0
    curPos = toSplit.find(delimiter)
    matchFound = curPos != -1

    while matchFound :
        splitList.append(toSplit[prevPos:curPos])
        prevPos = curPos + 1
        curPos = toSplit.find(delimiter,prevPos)
        matchFound = curPos != -1

    # so, if no more values were found, but previous ones were, then we need to load the final segment
    if curPos == -1 and prevPos != 0 :
        splitList.append(toSplit[prevPos:]) #assumes prevPos to end of string

    return splitList

# Purpose: add the duration to the startTime and return a new time in the format of "h:mm [AM/PM]" + "", " (next day)", or " ([x] days later)"
def add_time(startTime,duration,day=None) : 
    # 1) Create class instance to store time values, store as military time
    newTime = time(time=startTime,day=day)
    # 2) add time... the duration will be formatted as [hours]:[minutes]
    hourMinute = strSplit(duration,":")
    newTime.addHours(numHours=int(hourMinute[0]))
    newTime.addMinutes(numMinutes=int(hourMinute[1]))
    # 3) get the formatted time and return it
    return newTime.getFormattedTime()