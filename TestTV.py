#import classtv file
from ClassTV import TV
#create class
def TestTV():
    # creates two TV objects and tests their methods
    tv1 = TV(1, 1, True)
    tv1.setChannel(30)
    tv1.setVolume(3)
    print(f"You are now watching channel {tv1.getChannel()} on TV1 and its volume level is {tv1.getVolume()}")

    tv2 = TV(1, 1, True)
    tv2.setChannel(3)
    tv2.setVolume(2)
    print(f"You are now watching channel {tv2.getChannel()} on TV and its volume level is {tv2.getVolume()}")

TestTV()