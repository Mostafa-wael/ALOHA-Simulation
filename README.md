# ALOHA SImulation

## Introduction to ALOHA:
ALOHA is a multiple access protocol for transmission of data via a shared network channel. 
It operates in the medium access control sublayer (MAC sublayer) of the open systems interconnection (OSI) model. 
Using this protocol, several data streams originating from multiple nodes are transferred through a multi-point transmission channel.
In ALOHA, each station can transmit at any time, and frames are transmitted with some probability.
If two or more frames collide, they are retransmitted after a random delay.


## Unslotted ALOHA:
- In unslotted ALOHA, each station can transmit at any time.
- Frames are transmitted with some probability P.
- The probability of a successful transmission is given by `P(1 - P)^(N-1)`, where N is the number of stations.

## Slotted ALOHA:
- In slotted ALOHA, frames can only be transmitted at the start of each time slot.
- Each time slot is equal to the length of a frame transmission time, denoted by M.
- Frames are transmitted with some probability P.
- The probability of a successful transmission is given by `P(1 - P)^(N-1)`.

## Comparing Slotted and Unslotted ALOHA:
- Slotted ALOHA is more efficient than unslotted ALOHA.
- The maximum achievable throughput in slotted ALOHA is approximately **0.37**, while in unslotted ALOHA it is approximately **0.18**.
- Slotted ALOHA has a higher probability of successful transmission because frames are only transmitted at the start of each time slot.
- In unslotted ALOHA, there is a higher probability of collision because frames can be transmitted at any time.
- However, slotted ALOHA requires synchronization between nodes and can lead to idle slots if a node has no data to transmit.
  
## Effect of the Number of Stations:
- As the number of stations increases, the throughput of both slotted and unslotted ALOHA decreases.
- This is because the probability of collision increases as more stations attempt to transmit at the same time.
- However, slotted ALOHA is less affected by the number of stations because collisions are less likely due to the synchronized time slots.

## Effect of the Frame Transmission Time:
- The optimal frame transmission time for both slotted and unslotted ALOHA is dependent on the number of stations.
- For unslotted ALOHA, the maximum achievable throughput is given by `N*P(1 - P)^(N-1)` at `M = 1/P`.
- For slotted ALOHA, the maximum achievable throughput is given by `N*P(1 - P)^(N-1)` at `M = 1/(2P)`.

![](output/Throughput%20vs.%20M%20for%20ALOHA%20with%20P=0.05,%20N=10,%20T=10000.png)
![](output/Throughput%20vs.%20N%20for%20ALOHA%20with%20P=0.5,%20M=1,%20T=10000.png)
