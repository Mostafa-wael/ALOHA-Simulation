import random
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
    
def simulateAloha(numStations, transmissionProb, frameTransTime, totalSimTime, slotted=False):
    # Initialize the simulation state
    state = [0] * numStations # 0 represents idle, 1 represents transmitting
    frames = [0] * numStations # frames waiting to be transmitted
    delay = [0] * numStations # delay of the current frame
    successfulTransmissions = 0 # count of successfully transmitted frames
    collisions = 0 # count of collisions
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
                    continue # not a valid time slot
                state[i] = 1 # start transmitting
                frames[i] -= 1 # decrement the number of frames to transmit
        # Check for collisions
        activeStations = sum(state) # number of stations transmitting
        if activeStations > 1: # if more than one station is transmitting
            collisions += 1
            for i in range(numStations):
                # if the station is transmitting
                if state[i] == 1:
                    frames[i] += 1 # increment the number of frames to transmit
                    state[i] = 0 # stop transmitting
                    delay[i] += random.randint(0, 10) * frameTransTime # set a random delay
        elif activeStations == 1: # if exactly one station is transmitting
            successfulTransmissions += 1
            for i in range(numStations):
                if state[i] == 1: # if the station is transmitting
                    state[i] = 0 # stop transmitting

    return successfulTransmissions, collisions, state

def plot_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False):
    throughputValues = []
    for N in tqdm(numStationsValues):
        successfulTransmissions, collisions, _ = simulateAloha(N, transmissionProb, frameTransTime, totalSimTime, slotted)
        throughput = successfulTransmissions / totalSimTime
        throughputValues.append(throughput)
    plt.figure()
    plt.plot(numStationsValues, throughputValues)
    plt.xlabel('Number of Stations')
    plt.ylabel('Throughput')
    title = 'Throughput vs. N for {}-ALOHA with P={} and M={}'.format('slotted' if slotted else 'unslotted', transmissionProb, frameTransTime)
    plt.title(title)
    # plt.show()
    plt.savefig('output/' + title + '.png')


def plot_throughput_vs_M(numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False):
    throughputValues = []
    for frameTransTime in tqdm(frameTransTimeValues):
        successfulTransmissions, _, _ = simulateAloha(numStations, transmissionProb, frameTransTime, totalSimTime, slotted)
        throughput = successfulTransmissions / totalSimTime
        throughputValues.append(throughput)
    plt.figure()
    plt.plot(frameTransTimeValues, throughputValues)
    plt.xlabel('Frame Transmission Time')
    plt.ylabel('Throughput')
    title = 'Throughput vs. M for {}-ALOHA with P={} and N={}'.format('slotted' if slotted else 'unslotted', transmissionProb, numStations)
    plt.title(title)
    # plt.show()
    plt.savefig('output/' + title + '.png')

def main():
    transmissionProb = 0.05 # probability of transmission
    totalSimTime = 100000 # total simulation time

    # Plot throughput vs. N for both unslotted and slotted ALOHA
    # numStationsValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    numStationsValues = list(range(10, 101, 10))
    frameTransTime = 1 # transmission time
    plot_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False)
    plot_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=True)

    # Plot throughput vs. M for both unslotted and slotted ALOHA
    numStations = 50 # number of stations
    # frameTransTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # transmission time values to test
    frameTransTimeValues = list(range(1, 101, 10)) # transmission time values to test
    maxThroughput = numStations * transmissionProb * (1 - transmissionProb) ** (numStations - 1)
    maxThroughputFrameTransTimeSlotted = 1 / (2 * transmissionProb)
    maxThroughputFrameTransTimeUnslotted = 1 / transmissionProb
    plot_throughput_vs_M(numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False)
    plot_throughput_vs_M(numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=True)
    print('Maximum throughput for unslotted ALOHA: {} at M = {}'.format(maxThroughput, maxThroughputFrameTransTimeUnslotted))
    print('Maximum throughput for slotted ALOHA: {} at M = {}'.format(maxThroughput, maxThroughputFrameTransTimeSlotted))
    
if __name__ == '__main__':
    main()
