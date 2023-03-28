import random


class Station:
    def __init__(self):
        self.frames = 0  # frames waiting to be transmitted
        self.state = 0  # 0 represents idle, 1 represents transmitting
        self.delay = 0  # delay of the current frame
        self.transTime = 0  # time remaining to transmit the current frame

    def generateFrames(self, transmissionProb):
        if random.random() < transmissionProb:
            self.frames += 1
            return True

    def transmit(self, frameTransTime, slotted, t):
        # if the station is idle and has frames to transmit
        # No need to check for the transmission time, because we can only send if the station is idle
        if self.frames > 0 and self.state == 0:
            # check if the station has a delay
            if self.delay > 0:
                self.delay -= 1
                return
            # if slotted ALOHA, only transmit at the beginning of a time slot
            if slotted and t % frameTransTime != 0:
                return  # not a valid time slot
            self.state = 1  # start transmitting
            # decrement the number of frames to transmit
            self.frames -= 1
            # set the transmission time
            self.transTime = frameTransTime

    def endTransmission(self, frameTransTime, slotted, t):
        # Check if the transmission is complete
        if self.transTime > 0:
            self.transTime -= 1
            return False
        else:
            self.state = 0  # stop transmitting
            self.transTime = 0  # reset the transmission time
            return True
            
    def cancelTransmission(self, frameTransTime, slotted, t):
        self.state = 0  # stop transmitting
        self.transTime = 0  # reset the transmission time
        self.frames += 1  # increment the number of frames to transmit
        # set a random delay, max delay is 10 time units
        if slotted:
            self.delay = random.randint(0, 10) * frameTransTime
        else:
            self.delay = random.randint(0, 10)



def simulateAloha(numStations, transmissionProb, frameTransTime, totalSimTime, slotted=False):
    # Initialize the simulation states
    stations = [Station() for i in range(numStations)]
    successfulTransmissions = 0  # count of successfully transmitted frames
    totalNumTransmissions = 0
    collisions = 0  # count of collisions
    # Simulate the ALOHA protocol for (totalSimTime) time units
    for t in range(totalSimTime):
        # Stations generate frames
        for s in stations:
            if s.generateFrames(transmissionProb):
                totalNumTransmissions += 1
        # Stations transmit frames if they have any
        random.shuffle(stations)
        for s in stations:
            s.transmit(frameTransTime, slotted, t)
            # break # Allow only one station to transmit in each time slot
        # Check for collisions
        activeStations = [s for s in stations if s.state == 1]
        numActiveStations = len(activeStations) # number of stations transmitting
        if numActiveStations > 1: # if more than one station is transmitting
            collisions += 1
            for s in activeStations: # cancel the transmission of all stations
                s.cancelTransmission(frameTransTime, slotted, t)
        elif numActiveStations == 1:  # if exactly one station is transmitting
            for s in activeStations: # end the transmission of the station
                if s.endTransmission(frameTransTime, slotted, t):
                    successfulTransmissions += 1

    return successfulTransmissions, collisions, totalNumTransmissions
