import random


def simulateAloha(numStations, transmissionProb, frameTransTime, totalSimTime, slotted=False):
    # Initialize the simulation state
    state = [0] * numStations  # 0 represents idle, 1 represents transmitting
    frames = [0] * numStations  # frames waiting to be transmitted
    delay = [0] * numStations  # delay of the current frame
    successfulTransmissions = 0  # count of successfully transmitted frames
    collisions = 0  # count of collisions
    # Simulate the ALOHA protocol for (totalSimTime) time units
    # show progress bar
    for t in range(totalSimTime):
        # Stations generate frames with probability (transmissionProb)
        for i in range(numStations):
            if random.random() < transmissionProb:
                frames[i] += 1
        # Stations transmit frames if they have any
        for i in range(numStations):
            # if the station is idle and has frames to transmit
            if frames[i] > 0 and state[i] == 0:
                # check if the station is in the delay period
                if delay[i] > 0:
                    delay[i] -= 1
                    continue
                # if slotted ALOHA, onl y transmit at the beginning of a time slot
                if slotted and t % frameTransTime != 0:
                    continue  # not a valid time slot
                state[i] = 1  # start transmitting
                frames[i] -= 1  # decrement the number of frames to transmit
        # Check for collisions
        activeStations = sum(state)  # number of stations transmitting
        if activeStations > 1:  # if more than one station is transmitting
            collisions += 1
            for i in range(numStations):
                # if the station is transmitting
                if state[i] == 1:
                    # increment the number of frames to transmit
                    frames[i] += 1
                    state[i] = 0  # stop transmitting
                    # set a random delay
                    delay[i] += random.randint(0, 10) * frameTransTime
        elif activeStations == 1:  # if exactly one station is transmitting
            successfulTransmissions += 1
            for i in range(numStations):
                if state[i] == 1:  # if the station is transmitting
                    state[i] = 0  # stop transmitting

    return successfulTransmissions, collisions, state



