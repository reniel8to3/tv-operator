#create class
class TV:
#create tv attributes
    def __init__(self, channel, volumeLevel, on):
            self.channel = channel
            self.volumeLevel = volumeLevel
            self.on = on
#create on and off functions
    def turnOn(self):
        self.on = True
    def turnOff(self):
        self.on = False
    #create channel function
    def getChannel(self):
        return self.channel
    #create set channel function 
    def getVolume(self):
        return self.volumeLevel
    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel
    #channel up and down
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    #volume up and down
    def volumeUp(self):
        self.volumeLevel += 1
    def volumeDown(self):
        self.volumeLevel -= 1
    