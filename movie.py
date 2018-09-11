class Movie:
    def __init__(self, name, runTime, screenFormatStartTimesDict):
        self.name = name
        self.runTime = runTime
        self.screenFormatStartTimesDict = screenFormatStartTimesDict

    def print(self):
        print(self.name + ': ' + self.runTime)
        for screenFormat, screenFormatStartTimesDict in self.screenFormatStartTimesDict.items():
            for startTime in screenFormatStartTimesDict:
                print(screenFormat + ' -- ' + startTime)