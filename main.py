from aloha import simulateAloha
from plotting import plot_throughput_vs_N, plot_throughput_vs_M, plot_throughput_vs_MM


def main():
    transmissionProb = 0.05  # probability of transmission
    totalSimTime = 10000  # total simulation time

    # Plot throughput vs. N for both unslotted and slotted ALOHA
    numStationsValues = list(range(10, 101, 20))
    frameTransTime = 1  # transmission time
    plot_throughput_vs_N(numStationsValues, transmissionProb,
                         frameTransTime, totalSimTime)
    plot_throughput_vs_N(numStationsValues, transmissionProb,
                         frameTransTime, totalSimTime)

    # Plot throughput vs. M for both unslotted and slotted ALOHA
    numStations = 10  # number of stations
    # transmission time values to test
    frameTransTimeValues = list(range(1, 51, 5))
    maxThroughput = numStations * transmissionProb * \
        (1 - transmissionProb) ** (numStations - 1)
    maxThroughputFrameTransTimeSlotted = 1 / (2 * transmissionProb)
    maxThroughputFrameTransTimeUnslotted = 1 / transmissionProb
    plot_throughput_vs_M(numStations, transmissionProb,
                         frameTransTimeValues, totalSimTime)
    plot_throughput_vs_M(numStations, transmissionProb,
                         frameTransTimeValues, totalSimTime)
    plot_throughput_vs_MM(numStations, transmissionProb,
                         frameTransTimeValues, totalSimTime)
    print('Maximum throughput for unslotted ALOHA: {} at M = {} and P = {}'.format(
        maxThroughput, maxThroughputFrameTransTimeUnslotted, transmissionProb))
    print('Maximum throughput for slotted ALOHA: {} at M = {} and P = {}'.format(
        maxThroughput, maxThroughputFrameTransTimeSlotted, transmissionProb))


if __name__ == '__main__':
    main()