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
    def setChannel(self, channel):
        self.channel = channel
        if self.channel > 100 or self.channel < 1:
            print("TV's channel is out of range.")
        else:
            return self.channel
    def getVolume(self):
        return self.volumeLevel
    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel
        if self.volumeLevel > 60 or self.volumeLevel < 1:
            print("TV's volume is out of range.")
        else:
            return self.volumeLevel
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
    