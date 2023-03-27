import matplotlib.pyplot as plt
from tqdm.auto import tqdm
from aloha import simulateAloha


def get_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted):
    throughputValues = []
    for N in tqdm(numStationsValues, desc='N'):
        successfulTransmissions, collisions, totalNumTransmissions = simulateAloha(
            N, transmissionProb, frameTransTime, totalSimTime, slotted)
        throughput = successfulTransmissions / totalNumTransmissions
        throughputValues.append(throughput)
    return throughputValues


def plot_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime):
    throughputValues_slotted = get_throughput_vs_N(
        numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False)
    throughputValues_unslotted = get_throughput_vs_N(
        numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=True)
    # plot the results in the same figure
    plt.figure()
    plt.plot(numStationsValues, throughputValues_slotted, label='slotted')
    plt.plot(numStationsValues, throughputValues_unslotted, label='unslotted')
    plt.xlabel('Number of Stations')
    plt.ylabel('Throughput')
    title = 'Throughput vs. N for ALOHA with P={}, M={}, T={}'.format(
        transmissionProb, frameTransTime, totalSimTime)
    plt.title(title)
    plt.legend()
    # plt.show()
    plt.savefig('output/' + title + '.png')


def get_throughput_vs_M(numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted):
    throughputValues = []
    for frameTransTime in tqdm(frameTransTimeValues, desc='M'):
        successfulTransmissions, collisions, totalNumTransmissions = simulateAloha(
            numStations, transmissionProb, frameTransTime, totalSimTime, slotted)
        throughput = successfulTransmissions / totalNumTransmissions
        throughputValues.append(throughput)
    return throughputValues


def plot_throughput_vs_M(numStations, transmissionProb, frameTransTimeValues, totalSimTime):
    throughputValues_slotted = get_throughput_vs_M(
        numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False)
    throughputValues_unslotted = get_throughput_vs_M(
        numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=True)
    plt.figure()
    plt.plot(frameTransTimeValues, throughputValues_slotted, label='slotted')
    plt.plot(frameTransTimeValues, throughputValues_unslotted, label='unslotted')
    plt.xlabel('Frame Transmission Time')
    plt.ylabel('Throughput')
    title = 'Throughput vs. M for ALOHA with P={}, N={}, T={}'.format(
        transmissionProb, numStations, totalSimTime)
    plt.title(title)
    plt.legend()
    # plt.show()
    plt.savefig('output/' + title + '.png')

# def plot_throughput_vs_N(numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False):
#     throughputValues = []
#     for N in tqdm(numStationsValues):
#         successfulTransmissions, collisions, _ = simulateAloha(N, transmissionProb, frameTransTime, totalSimTime, slotted)
#         throughput = successfulTransmissions / totalSimTime
#         throughputValues.append(throughput)
#     plt.figure()
#     plt.plot(numStationsValues, throughputValues)
#     plt.xlabel('Number of Stations')
#     plt.ylabel('Throughput')
#     title = 'Throughput vs. N for {}-ALOHA with P={} and M={}'.format('slotted' if slotted else 'unslotted', transmissionProb, frameTransTime)
#     plt.title(title)
#     # plt.show()
#     plt.savefig('output/' + title + '.png')


# def plot_throughput_vs_MM(numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False):
#     throughputValues = []
#     for frameTransTime in tqdm(frameTransTimeValues):
#         successfulTransmissions, _, _ = simulateAloha(
#             numStations, transmissionProb, frameTransTime, totalSimTime, slotted)
#         throughput = successfulTransmissions / totalSimTime
#         throughputValues.append(throughput)
#     plt.figure()
#     plt.plot(frameTransTimeValues, throughputValues)
#     plt.xlabel('Frame Transmission Time')
#     plt.ylabel('Throughput')
#     title = 'Throughput vs. M for {}-ALOHA with P={} and N={}'.format(
#         'slotted' if slotted else 'unslotted', transmissionProb, numStations)
#     plt.title(title)
#     plt.show()
#     plt.savefig('output/' + title + '.png')
