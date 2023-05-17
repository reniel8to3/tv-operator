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
    #volume up and down

    #channel up and down
