class Station:
    # the station class represents a station in the network
    def __init__(self, id, transmissionProb, frameTransTime, totalSimTime):
        self.id = id
        self.transmissionProb = transmissionProb
        self.frameTransTime = frameTransTime
        self.totalSimTime = totalSimTime
        self.state = 0 # 0 represents idle, 1 represents transmitting
        self.frames = 0 # frames waiting to be transmitted
        self.delay = 0 # delay of the current frame
        self.successfulTransmissions = 0 # count of successfully transmitted frames
        self.collisions = 0 # count of collisions
    def generateFrames(self):
        if random.random() < transmissionProb:
                frames[i] += 1
    def transmitFrames(self, slotted):
        # if the station is idle and has frames to transmit
        if self.frames > 0 and self.state == 0:
            # check if the station is in the delay period
            if self.delay > 0:
                self.delay -= 1
                return
            # if slotted ALOHA, only transmit at the beginning of a time slot
            if slotted and t % self.frameTransTime != 0:
                return
            self.state = 1 # start transmitting
            self.frames -= 1 # decrement the number of frames to transmit
    def checkForCollisions(self, activeStations):
        if activeStations > 1:
            self.collisions += 1
            self.frames += 1
            self.state = 0
            self.delay += random.randint(0, self.frameTransTime - 1)
        elif activeStations == 1:
            self.successfulTransmissions += 1
            self.state = 0
    def simulateAloha(self, slotted):
        for t in range(self.totalSimTime):
            self.generateFrames()
            self.transmitFrames(slotted)
            activeStations = sum([station.state for station in stations])
            self.checkForCollisions(activeStations)
        return self.successfulTransmissions, self.collisions, self.state
    def plot_throughput_vs_N(self, numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False):
        throughputValues = []
        for N in tqdm(numStationsValues):
            successfulTransmissions, collisions, _ = simulateAloha(N, transmissionProb, frameTransTime, totalSimTime, slotted)
            throughput = successfulTransmissions / totalSimTime
            throughputValues.append(throughput)
        plt.figure()
        plt.plot(numStationsValues, throughputValues)
        plt.xlabel('N')
        plt.ylabel('Throughput')
        title = 'Throughput vs. N for {}-ALOHA with P={} and M={}'.format('slotted' if slotted else 'unslotted', transmissionProb, frameTransTime)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_throughput_vs_P(self, numStations, transmissionProbValues, frameTransTime, totalSimTime, slotted=False):
        throughputValues = []
        for P in tqdm(transmissionProbValues):
            successfulTransmissions, collisions, _ = simulateAloha(numStations, P, frameTransTime, totalSimTime, slotted)
            throughput = successfulTransmissions / totalSimTime
            throughputValues.append(throughput)
        plt.figure()
        plt.plot(transmissionProbValues, throughputValues)
        plt.xlabel('P')
        plt.ylabel('Throughput')
        title = 'Throughput vs. P for {}-ALOHA with N={} and M={}'.format('slotted' if slotted else 'unslotted', numStations, frameTransTime)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_throughput_vs_M(self, numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False):
        throughputValues = []
        for M in tqdm(frameTransTimeValues):
            successfulTransmissions, collisions, _ = simulateAloha(numStations, transmissionProb, M, totalSimTime, slotted)
            throughput = successfulTransmissions / totalSimTime
            throughputValues.append(throughput)
        plt.figure()
        plt.plot(frameTransTimeValues, throughputValues)
        plt.xlabel('M')
        plt.ylabel('Throughput')
        title = 'Throughput vs. M for {}-ALOHA with N={} and P={}'.format('slotted' if slotted else 'unslotted', numStations, transmissionProb)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_collisions_vs_N(self, numStationsValues, transmissionProb, frameTransTime, totalSimTime, slotted=False):
        collisionValues = []
        for N in tqdm(numStationsValues):
            successfulTransmissions, collisions, _ = simulateAloha(N, transmissionProb, frameTransTime, totalSimTime, slotted)
            collisionValues.append(collisions)
        plt.figure()
        plt.plot(numStationsValues, collisionValues)
        plt.xlabel('N')
        plt.ylabel('Collisions')
        title = 'Collisions vs. N for {}-ALOHA with P={} and M={}'.format('slotted' if slotted else 'unslotted', transmissionProb, frameTransTime)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_collisions_vs_P(self, numStations, transmissionProbValues, frameTransTime, totalSimTime, slotted=False):
        collisionValues = []
        for P in tqdm(transmissionProbValues):
            successfulTransmissions, collisions, _ = simulateAloha(numStations, P, frameTransTime, totalSimTime, slotted)
            collisionValues.append(collisions)
        plt.figure()
        plt.plot(transmissionProbValues, collisionValues)
        plt.xlabel('P')
        plt.ylabel('Collisions')
        title = 'Collisions vs. P for {}-ALOHA with N={} and M={}'.format('slotted' if slotted else 'unslotted', numStations, frameTransTime)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_collisions_vs_M(self, numStations, transmissionProb, frameTransTimeValues, totalSimTime, slotted=False):
        collisionValues = []
        for M in tqdm(frameTransTimeValues):
            successfulTransmissions, collisions, _ = simulateAloha(numStations, transmissionProb, M, totalSimTime, slotted)
            collisionValues.append(collisions)
        plt.figure()
        plt.plot(frameTransTimeValues, collisionValues)
        plt.xlabel('M')
        plt.ylabel('Collisions')
        title = 'Collisions vs. M for {}-ALOHA with N={} and P={}'.format('slotted' if slotted else 'unslotted', numStations, transmissionProb)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))
    def plot_collisions_vs_throughput(self, numStations, transmissionProb, frameTransTime, totalSimTime, slotted=False):
        collisionValues = []
        throughputValues = []
        for N in tqdm(numStations):
            successfulTransmissions, collisions, _ = simulateAloha(N, transmissionProb, frameTransTime, totalSimTime, slotted)
            collisionValues.append(collisions)
            throughput = successfulTransmissions / totalSimTime
            throughputValues.append(throughput)
        plt.figure()
        plt.plot(throughputValues, collisionValues)
        plt.xlabel('Throughput')
        plt.ylabel('Collisions')
        title = 'Collisions vs. Throughput for {}-ALOHA with N={} and P={}'.format('slotted' if slotted else 'unslotted', numStations, transmissionProb)
        plt.title(title)
        # plt.show()
        plt.savefig('{}.png'.format(title))

def main():
    