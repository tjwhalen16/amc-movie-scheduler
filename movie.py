class Movie:
    def __init__(self, name, runTime, screenFormat, startTime):
        self.name = name
        self.runTime = runTime
        self.screenFormat = screenFormat
        self.startTime = startTime

    def print(self):
        print(self.name + ': ' + self.runTime + ' @ ' + self.startTime + ' in ' + self.screenFormat)