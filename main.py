from aloha import simulateAloha
from plotting import plot_throughput_vs_N, plot_throughput_vs_M


def main():
    totalSimTime = 10000  # total simulation time
    ########################################
    # Plot throughput vs. M for both unslotted and slotted ALOHA
    transmissionProb = 0.05  # probability of transmission
    numStations = 10  # number of stations
    frameTransTimeValues = list(range(1, 26, 1))
    plot_throughput_vs_M(numStations, transmissionProb,
                         frameTransTimeValues, totalSimTime)

    ########################################
    # Plot throughput vs. N for both unslotted and slotted ALOHA
    transmissionProb = 0.5  # probability of transmission
    numStationsValues = list(range(1, 51, 1))
    frameTransTime = 1  # transmission time
    plot_throughput_vs_N(numStationsValues, transmissionProb,
                         frameTransTime, totalSimTime)

    ########################################
    # Find the maximum throughput for both unslotted and slotted ALOHA
    maxThroughput = numStations * transmissionProb * \
        (1 - transmissionProb) ** (numStations - 1)
    maxThroughputFrameTransTimeSlotted = 1 / (2 * transmissionProb)
    maxThroughputFrameTransTimeUnslotted = 1 / transmissionProb
    print('Maximum throughput for unslotted ALOHA with P = {}: {} at M = {}'.format(
        maxThroughput, transmissionProb, maxThroughputFrameTransTimeUnslotted))
    print('Maximum throughput for slotted ALOHA with P = {}: {} at M = {}'.format(
        maxThroughput, transmissionProb, maxThroughputFrameTransTimeSlotted))


if __name__ == '__main__':
    main()
